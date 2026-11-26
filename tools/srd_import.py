"""Import SRD 5.1 content from the D&D 5e API into data/, in our own format.

    uv run python tools/srd_import.py

The API (https://www.dnd5eapi.co) serves both the 2014 and 2024 rules; we only read the 2014
endpoints. Each record is converted to our schemas (fantasygame.content.schemas), tagged
`"source": "srd-5.1"`, and written to data/<folder>/<id>.json. Re-running replaces SRD files and
removes SRD files the API no longer has; files with any other source are never touched. The
whole data folder is loaded and checked at the end.

Not imported yet: rules mechanics (breath weapons, the high elf's cantrip choice, class levels
and features), which come with the features and effects system, and equipment.
"""

import json
import sys
import time
import urllib.request
from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from fantasygame.content.data import DATA_DIR, load_game_data
from fantasygame.content.schemas import (
    Ability,
    AbilityBonusChoice,
    AbilityInfo,
    AbilityMinimum,
    Background,
    BackgroundFeature,
    CharacterClass,
    Choice,
    Grants,
    Language,
    LanguageChoice,
    Multiclassing,
    Proficiency,
    ProficiencyChoice,
    Race,
    Record,
    Skill,
    SkillChoice,
    Source,
    Subrace,
    Trait,
    TraitChoice,
)

API = "https://www.dnd5eapi.co/api/2014"
SRD = Source.SRD_5_1

type Raw = dict[str, Any]


# --- Fetching ---


def fetch(path: str) -> Any:
    request = urllib.request.Request(f"{API}/{path}", headers={"User-Agent": "fantasygame"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except OSError:
            if attempt == 3:
                raise
            time.sleep(2**attempt)


def fetch_all(endpoint: str) -> list[Raw]:
    indexes = [r["index"] for r in fetch(endpoint)["results"]]
    with ThreadPoolExecutor(max_workers=8) as pool:
        return list(pool.map(lambda i: fetch(f"{endpoint}/{i}"), indexes))


# --- Converting helpers ---


def fix_text(text: str) -> str:
    """Repair UTF-8 text that was decoded as Windows-1252 somewhere upstream ("â€™" -> "’")."""
    if "â" in text or "Ã" in text:
        try:
            return text.encode("cp1252").decode("utf-8")
        except UnicodeError:
            pass
    return text


def paragraphs(desc: str | list[str] | None) -> str:
    if desc is None:
        return ""
    if isinstance(desc, str):
        desc = [desc]
    return "\n\n".join(fix_text(p) for p in desc)


def option_indexes(option_set: Raw) -> list[str]:
    """The ids in an API option set. Nested choices ("a tool or an instrument") are flattened."""
    indexes: list[str] = []
    for option in option_set["options"]:
        if option["option_type"] == "reference":
            indexes.append(option["item"]["index"])
        elif option["option_type"] == "choice":
            indexes.extend(option_indexes(option["choice"]["from"]))
        else:
            raise ValueError(f"Unexpected option type {option['option_type']!r}")
    return indexes


def option_strings(raw: Raw | None) -> list[str]:
    if raw is None:
        return []
    return [fix_text(o.get("string") or o["desc"]) for o in raw["from"]["options"]]


def is_skill(proficiency_id: str) -> bool:
    return proficiency_id.startswith("skill-")


def is_saving_throw(proficiency_id: str) -> bool:
    return proficiency_id.startswith("saving-throw-")


def skill_id(proficiency_id: str) -> str:
    return proficiency_id.removeprefix("skill-")


def grants_from(
    proficiencies: Sequence[Raw] = (),
    languages: Sequence[Raw] = (),
    choices: Sequence[Choice] = (),
) -> Grants:
    """Split API proficiency references into skills and other proficiencies.

    Saving throw proficiencies are dropped: classes list them in `saving_throws`.
    """
    ids = [p["index"] for p in proficiencies]
    return Grants(
        skills=[skill_id(i) for i in ids if is_skill(i)],
        proficiencies=[i for i in ids if not is_skill(i) and not is_saving_throw(i)],
        languages=[lang["index"] for lang in languages],
        choices=list(choices),
    )


NOT_ARTISANS_TOOLS = {"disguise-kit", "forgery-kit"}
"""The API files these under artisan's tools, so they show up in the monk's "artisan's tools or
a musical instrument" choice. In the SRD they are not artisan's tools."""


def proficiency_choice(raw: Raw) -> Choice:
    ids = [i for i in option_indexes(raw["from"]) if i not in NOT_ARTISANS_TOOLS]
    if all(is_skill(i) for i in ids):
        return SkillChoice(kind="skill", choose=raw["choose"], options=[skill_id(i) for i in ids])
    if any(is_skill(i) for i in ids):
        raise ValueError(f"Choice mixes skills and other proficiencies: {ids}")
    return ProficiencyChoice(kind="proficiency", choose=raw["choose"], options=ids)


def language_choice(raw: Raw) -> LanguageChoice:
    if raw["from"]["option_set_type"] == "resource_list":  # any language
        return LanguageChoice(kind="language", choose=raw["choose"])
    return LanguageChoice(
        kind="language", choose=raw["choose"], options=option_indexes(raw["from"])
    )


def ability_bonuses(raw: list[Raw]) -> dict[Ability, int]:
    return {srd_ability(b["ability_score"]["index"]): b["bonus"] for b in raw}


def ability_minimums(raw: Sequence[Raw]) -> list[AbilityMinimum]:
    return [
        AbilityMinimum(ability=srd_ability(p["ability_score"]["index"]), score=p["minimum_score"])
        for p in raw
    ]


# --- Converting records ---


SRD_ABILITY_CODES = {"str", "dex", "con", "int", "wis", "cha"}


def srd_ability(code: str) -> Ability:
    """The API names abilities by short code (`con`); our ids are full names (`constitution`)."""
    if code not in SRD_ABILITY_CODES:
        raise ValueError(f"unknown ability code {code!r}")
    return Ability[code.upper()]


def convert_ability(raw: Raw) -> AbilityInfo:
    return AbilityInfo(
        id=srd_ability(raw["index"]).value,
        name=raw["full_name"],
        source=SRD,
        description=paragraphs(raw["desc"]),
        abbreviation=raw["name"],
    )


def convert_skill(raw: Raw) -> Skill:
    return Skill(
        id=raw["index"],
        name=raw["name"],
        source=SRD,
        description=paragraphs(raw["desc"]),
        ability=srd_ability(raw["ability_score"]["index"]),
    )


def convert_language(raw: Raw) -> Language:
    return Language(
        id=raw["index"],
        name=raw["name"],
        source=SRD,
        description=paragraphs(raw.get("desc")),
        kind=raw["type"].lower(),
        script=raw.get("script"),
        typical_speakers=raw["typical_speakers"],
    )


PROFICIENCY_KINDS = {
    "Armor": "armor",
    "Weapons": "weapon",
    "Artisan's Tools": "tool",
    "Other": "tool",  # herbalism kit, navigator's tools, poisoner's kit, thieves' tools
    "Musical Instruments": "instrument",
    "Gaming Sets": "gaming-set",
    "Vehicles": "vehicle",
}


def convert_proficiency(raw: Raw) -> Proficiency | None:
    if raw["type"] in ("Skills", "Saving Throws"):
        return None  # these refer to skills and abilities directly
    return Proficiency(
        id=raw["index"],
        name=fix_text(raw["name"]),
        source=SRD,
        kind=PROFICIENCY_KINDS[raw["type"]],  # pyright: ignore[reportArgumentType]
    )


def convert_trait(raw: Raw) -> Trait:
    choices: list[Choice] = []
    if "proficiency_choices" in raw:
        choices.append(proficiency_choice(raw["proficiency_choices"]))
    if "language_options" in raw:
        choices.append(language_choice(raw["language_options"]))
    subtraits = raw.get("trait_specific", {}).get("subtrait_options")
    if subtraits:
        choices.append(
            TraitChoice(
                kind="trait", choose=subtraits["choose"], options=option_indexes(subtraits["from"])
            )
        )
    return Trait(
        id=raw["index"],
        name=fix_text(raw["name"]),
        source=SRD,
        description=paragraphs(raw["desc"]),
        parent=raw["parent"]["index"] if raw.get("parent") else None,
        grants=grants_from(proficiencies=raw["proficiencies"], choices=choices),
    )


def convert_race(raw: Raw) -> Race:
    bonus_choices: list[AbilityBonusChoice] = []
    if "ability_bonus_options" in raw:
        options = raw["ability_bonus_options"]["from"]["options"]
        bonuses = {o["bonus"] for o in options}
        if len(bonuses) != 1:
            raise ValueError(f"{raw['index']}: ability bonus options differ: {bonuses}")
        bonus_choices.append(
            AbilityBonusChoice(
                choose=raw["ability_bonus_options"]["choose"],
                bonus=bonuses.pop(),
                options=[srd_ability(o["ability_score"]["index"]) for o in options],
            )
        )
    choices: list[Choice] = []
    if "language_options" in raw:
        choices.append(language_choice(raw["language_options"]))
    return Race(
        id=raw["index"],
        name=raw["name"],
        source=SRD,
        description=paragraphs(
            [raw[k] for k in ("age", "alignment", "size_description", "language_desc")]
        ),
        size=raw["size"].lower(),
        speed=raw["speed"],
        ability_bonuses=ability_bonuses(raw["ability_bonuses"]),
        ability_bonus_choices=bonus_choices,
        traits=[t["index"] for t in raw["traits"]],
        grants=grants_from(languages=raw["languages"], choices=choices),
    )


def convert_subrace(raw: Raw) -> Subrace:
    return Subrace(
        id=raw["index"],
        name=raw["name"],
        source=SRD,
        description=paragraphs(raw["desc"]),
        race=raw["race"]["index"],
        ability_bonuses=ability_bonuses(raw["ability_bonuses"]),
        traits=[t["index"] for t in raw["racial_traits"]],
    )


def convert_background(raw: Raw) -> Background:
    choices: list[Choice] = []
    if "language_options" in raw:
        choices.append(language_choice(raw["language_options"]))
    gold = raw.get("starting_gold", {"quantity": 0, "unit": "gp"})
    if gold["unit"] != "gp":
        raise ValueError(f"{raw['index']}: starting gold in {gold['unit']!r}")
    return Background(
        id=raw["index"],
        name=raw["name"],
        source=SRD,
        grants=grants_from(proficiencies=raw["starting_proficiencies"], choices=choices),
        feature=BackgroundFeature(
            name=raw["feature"]["name"], description=paragraphs(raw["feature"]["desc"])
        ),
        starting_gold=gold["quantity"],
        personality_traits=option_strings(raw.get("personality_traits")),
        ideals=option_strings(raw.get("ideals")),
        bonds=option_strings(raw.get("bonds")),
        flaws=option_strings(raw.get("flaws")),
    )


def convert_class(raw: Raw) -> CharacterClass:
    multi = raw["multi_classing"]
    requires_any = multi.get("prerequisite_options")
    spellcasting = raw.get("spellcasting")
    return CharacterClass(
        id=raw["index"],
        name=raw["name"],
        source=SRD,
        hit_die=raw["hit_die"],
        saving_throws=[srd_ability(s["index"]) for s in raw["saving_throws"]],
        grants=grants_from(
            proficiencies=raw["proficiencies"],
            choices=[proficiency_choice(c) for c in raw["proficiency_choices"]],
        ),
        spellcasting_ability=(
            srd_ability(spellcasting["spellcasting_ability"]["index"]) if spellcasting else None
        ),
        multiclassing=Multiclassing(
            requires_all=ability_minimums(multi.get("prerequisites", [])),
            requires_any=ability_minimums(requires_any["from"]["options"] if requires_any else []),
            grants=grants_from(
                proficiencies=multi.get("proficiencies", []),
                choices=[proficiency_choice(c) for c in multi.get("proficiency_choices", [])],
            ),
        ),
    )


IMPORTS: dict[str, tuple[str, Callable[[Raw], Record | None]]] = {
    "abilities": ("ability-scores", convert_ability),
    "skills": ("skills", convert_skill),
    "languages": ("languages", convert_language),
    "proficiencies": ("proficiencies", convert_proficiency),
    "traits": ("traits", convert_trait),
    "races": ("races", convert_race),
    "subraces": ("subraces", convert_subrace),
    "backgrounds": ("backgrounds", convert_background),
    "classes": ("classes", convert_class),
}
"""Data folder -> (API endpoint, converter)."""


# --- Writing ---


def to_json(record: Record) -> str:
    raw = record.model_dump(mode="json", exclude_defaults=True)
    return json.dumps(raw, indent=2, ensure_ascii=False) + "\n"


def write_folder(data_dir: Path, folder: str, records: list[Record]) -> None:
    folder_dir = data_dir / folder
    folder_dir.mkdir(parents=True, exist_ok=True)
    new_ids = {r.id for r in records}
    for old in folder_dir.glob("*.json"):
        is_srd = json.loads(old.read_text(encoding="utf-8")).get("source") == SRD
        if is_srd and old.stem not in new_ids:
            old.unlink()
            print(f"  removed {folder}/{old.name}")
    for record in records:
        (folder_dir / f"{record.id}.json").write_text(to_json(record), encoding="utf-8")


def main(data_dir: Path = DATA_DIR) -> None:
    for folder, (endpoint, convert) in IMPORTS.items():
        records = [r for r in map(convert, fetch_all(endpoint)) if r is not None]
        write_folder(data_dir, folder, records)
        print(f"{folder}: {len(records)}")
    load_game_data(data_dir)
    print("All data loads and checks out.")


if __name__ == "__main__":
    sys.exit(main())

"""The SRD importer's conversions, on small hand-written API records (no network needed)."""

import json
from pathlib import Path

from fantasygame.content.schemas import Ability, ProficiencyChoice, Skill, SkillChoice, Source
from tools.srd_import import (
    convert_class,
    fix_text,
    proficiency_choice,
    srd_ability,
    write_folder,
)


def ref(index: str) -> dict:
    return {"option_type": "reference", "item": {"index": index}}


def choice(choose: int, *options: dict) -> dict:
    return {"choose": choose, "from": {"option_set_type": "options_array", "options": options}}


def test_mojibake_is_repaired() -> None:
    assert fix_text("artisanâ€™s tools") == "artisan’s tools"
    assert fix_text("plain text") == "plain text"


def test_skill_proficiencies_become_skill_ids() -> None:
    result = proficiency_choice(choice(2, ref("skill-arcana"), ref("skill-history")))
    assert result == SkillChoice(kind="skill", choose=2, options=["arcana", "history"])


def test_nested_choices_are_flattened_without_non_artisan_kits() -> None:
    tools = {"choose": 1, "from": choice(1, ref("smiths-tools"), ref("disguise-kit"))["from"]}
    nested = choice(1, {"option_type": "choice", "choice": tools}, ref("lute"))
    result = proficiency_choice(nested)
    assert result == ProficiencyChoice(
        kind="proficiency", choose=1, options=["smiths-tools", "lute"]
    )


def test_class_conversion() -> None:
    raw = {
        "index": "fighter",
        "name": "Fighter",
        "hit_die": 10,
        "saving_throws": [{"index": "str"}, {"index": "con"}],
        "proficiencies": [{"index": "all-armor"}, {"index": "saving-throw-str"}],
        "proficiency_choices": [choice(2, ref("skill-acrobatics"), ref("skill-athletics"))],
        "multi_classing": {
            "prerequisite_options": choice(
                1,
                {"ability_score": {"index": "str"}, "minimum_score": 13},
                {"ability_score": {"index": "dex"}, "minimum_score": 13},
            ),
            "proficiencies": [{"index": "light-armor"}],
        },
    }
    fighter = convert_class(raw)
    assert fighter.source == Source.SRD_5_1
    assert fighter.saving_throws == [Ability.STR, Ability.CON]
    assert fighter.grants.proficiencies == ["all-armor"]  # saving throws are not proficiencies
    assert [m.ability for m in fighter.multiclassing.requires_any] == [Ability.STR, Ability.DEX]
    assert fighter.multiclassing.requires_all == []


def test_reimport_removes_stale_srd_files_but_keeps_original_ones(tmp_path: Path) -> None:
    skills = tmp_path / "skills"
    skills.mkdir()
    (skills / "gone.json").write_text(json.dumps({"source": "srd-5.1"}), encoding="utf-8")
    (skills / "ours.json").write_text(json.dumps({"source": "original"}), encoding="utf-8")
    stealth = Skill(id="stealth", name="Stealth", source=Source.SRD_5_1, ability=Ability.DEX)

    write_folder(tmp_path, "skills", [stealth])

    assert sorted(p.name for p in skills.iterdir()) == ["ours.json", "stealth.json"]


def test_srd_ability_codes_become_full_name_ids() -> None:
    assert srd_ability("con") == Ability.CON == "constitution"
    assert [srd_ability(c) for c in ("str", "dex", "int", "wis", "cha")] == [
        "strength",
        "dexterity",
        "intelligence",
        "wisdom",
        "charisma",
    ]

"""Schemas for the game data in data/: what every record type looks like.

Plan choice #5: content lives in data files checked by these schemas, so a mistake is caught
when the game loads, not mid-fight. Every record carries a `source` (SRD 5.1 or original) so we
can always tell rules content from our own.

A field that names another record is typed as a reference, e.g. `SkillId`. The loader checks
that every reference points to a record that exists.

Rules mechanics (darkvision, breath weapons, class features) are not here yet: they arrive as
features and effects in Phase 1, piece 4.
"""

from dataclasses import dataclass
from enum import StrEnum
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Source(StrEnum):
    SRD_5_1 = "srd-5.1"
    """System Reference Document 5.1 (2014 rules), CC-BY-4.0. See data/ATTRIBUTION.md."""
    ORIGINAL = "original"
    """Written for this game."""


class Ability(StrEnum):
    STR = "strength"
    DEX = "dexterity"
    CON = "constitution"
    INT = "intelligence"
    WIS = "wisdom"
    CHA = "charisma"


# --- References ---


@dataclass(frozen=True)
class Ref:
    """Marks a field as naming a record in the data folder `folder`."""

    folder: str


SkillId = Annotated[str, Ref("skills")]
LanguageId = Annotated[str, Ref("languages")]
ProficiencyId = Annotated[str, Ref("proficiencies")]
TraitId = Annotated[str, Ref("traits")]
RaceId = Annotated[str, Ref("races")]


# --- Building blocks ---


class Model(BaseModel):
    # Unknown fields are errors (catches typos), and loaded data can't be changed by accident.
    model_config = ConfigDict(extra="forbid", frozen=True)


WINDOWS_RESERVED_NAMES = frozenset(
    ["con", "prn", "aux", "nul"] + [f"{d}{n}" for d in ("com", "lpt") for n in range(1, 10)]
)
"""Names Windows cannot use for a file, whatever the extension (con.json is not allowed)."""


class Record(Model):
    """Base of every record. One record per file: data/<folder>/<id>.json."""

    id: str = Field(pattern=r"^[a-z0-9]+(-[a-z0-9]+)*$")
    name: str = Field(min_length=1)
    source: Source
    description: str = ""

    @field_validator("id")
    @classmethod
    def _id_is_a_valid_file_name(cls, value: str) -> str:
        if value in WINDOWS_RESERVED_NAMES:
            raise ValueError(f"{value!r} is reserved by Windows and cannot be a file name")
        return value


class SkillChoice(Model):
    kind: Literal["skill"]
    choose: int = Field(ge=1)
    options: list[SkillId] | None = None
    """None means any skill."""


class ProficiencyChoice(Model):
    kind: Literal["proficiency"]
    choose: int = Field(ge=1)
    options: list[ProficiencyId]


class LanguageChoice(Model):
    kind: Literal["language"]
    choose: int = Field(ge=1)
    options: list[LanguageId] | None = None
    """None means any language."""


class TraitChoice(Model):
    kind: Literal["trait"]
    choose: int = Field(ge=1)
    options: list[TraitId]


Choice = Annotated[
    SkillChoice | ProficiencyChoice | LanguageChoice | TraitChoice, Field(discriminator="kind")
]


class Grants(Model):
    """What something gives a character: fixed proficiencies plus choices the player makes."""

    skills: list[SkillId] = []
    proficiencies: list[ProficiencyId] = []
    languages: list[LanguageId] = []
    choices: list[Choice] = []


class AbilityBonusChoice(Model):
    """E.g. the half-elf's "+1 to two other ability scores of your choice"."""

    choose: int = Field(ge=1)
    bonus: int
    options: list[Ability]


class AbilityMinimum(Model):
    ability: Ability
    score: int = Field(ge=1, le=30)


# --- Record types ---


class AbilityInfo(Record):
    """Name and description of an ability score. The rules use the `Ability` enum."""

    abbreviation: str


class Skill(Record):
    ability: Ability


class Language(Record):
    kind: Literal["standard", "exotic"]
    script: str | None = None
    typical_speakers: list[str] = []


class Proficiency(Record):
    """Armour, weapons, tools and the like. Skills and saving throws are not listed here."""

    kind: Literal["armor", "weapon", "tool", "instrument", "gaming-set", "vehicle"]


class Trait(Record):
    """A racial trait. `parent` is set on the variants of a trait, e.g. each draconic ancestry."""

    parent: TraitId | None = None
    grants: Grants = Grants()


class Race(Record):
    size: Literal["small", "medium"]
    speed: int = Field(gt=0)
    """Walking speed in feet."""
    ability_bonuses: dict[Ability, int] = {}
    ability_bonus_choices: list[AbilityBonusChoice] = []
    traits: list[TraitId] = []
    grants: Grants = Grants()


class Subrace(Record):
    race: RaceId
    ability_bonuses: dict[Ability, int] = {}
    traits: list[TraitId] = []


class BackgroundFeature(Model):
    name: str
    description: str


class Background(Record):
    grants: Grants = Grants()
    feature: BackgroundFeature
    starting_gold: int = 0
    personality_traits: list[str] = []
    ideals: list[str] = []
    bonds: list[str] = []
    flaws: list[str] = []


class Multiclassing(Model):
    """What you need to multiclass into a class, and what you get when you do."""

    requires_all: list[AbilityMinimum] = []
    requires_any: list[AbilityMinimum] = []
    """At least one of these, e.g. the fighter's Strength 13 or Dexterity 13."""
    grants: Grants = Grants()


class CharacterClass(Record):
    hit_die: Literal[6, 8, 10, 12]
    saving_throws: list[Ability]
    grants: Grants = Grants()
    spellcasting_ability: Ability | None = None
    multiclassing: Multiclassing


RECORD_TYPES: dict[str, type[Record]] = {
    "abilities": AbilityInfo,
    "skills": Skill,
    "languages": Language,
    "proficiencies": Proficiency,
    "traits": Trait,
    "races": Race,
    "subraces": Subrace,
    "backgrounds": Background,
    "classes": CharacterClass,
}
"""Each folder in data/ and the record type its files hold."""

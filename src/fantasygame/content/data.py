"""Loading the game data in data/ and checking it.

Every file is checked against its schema, its file name must match its `id`, and every
reference must point to a record that exists. All problems are collected and reported together,
so one load shows everything that needs fixing.
"""

import json
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from types import NoneType, UnionType
from typing import Annotated, Union, get_args, get_origin

from pydantic import BaseModel, ValidationError

from fantasygame.content.paths import install_dir
from fantasygame.content.schemas import (
    RECORD_TYPES,
    Ability,
    AbilityInfo,
    Background,
    CharacterClass,
    Language,
    Proficiency,
    Race,
    Record,
    Ref,
    Skill,
    Subrace,
    Trait,
)

DATA_DIR = install_dir() / "data"


class DataError(ValueError):
    pass


@dataclass(frozen=True)
class GameData:
    """All loaded records, by folder and then by id. Field names match RECORD_TYPES."""

    abilities: dict[str, AbilityInfo]
    skills: dict[str, Skill]
    languages: dict[str, Language]
    proficiencies: dict[str, Proficiency]
    traits: dict[str, Trait]
    races: dict[str, Race]
    subraces: dict[str, Subrace]
    backgrounds: dict[str, Background]
    classes: dict[str, CharacterClass]

    def folder(self, name: str) -> dict[str, Record]:
        return getattr(self, name)

    def subraces_of(self, race_id: str) -> list[Subrace]:
        return [s for s in self.subraces.values() if s.race == race_id]


def load_game_data(data_dir: Path = DATA_DIR) -> GameData:
    errors: list[str] = []

    for path in sorted(data_dir.iterdir()):
        if path.is_dir() and path.name not in RECORD_TYPES:
            errors.append(f"{path.name}/: unknown data folder")

    records: dict[str, dict[str, Record]] = {}
    for folder, model in RECORD_TYPES.items():
        records[folder] = {}
        for path in sorted((data_dir / folder).glob("*.json")):
            where = f"{folder}/{path.name}"
            try:
                record = model.model_validate(json.loads(path.read_text(encoding="utf-8")))
            except (json.JSONDecodeError, ValidationError) as e:
                errors.append(f"{where}: {e}")
                continue
            if record.id != path.stem:
                errors.append(f"{where}: id {record.id!r} does not match the file name")
                continue
            records[folder][record.id] = record

    if set(records["abilities"]) != {a.value for a in Ability}:
        errors.append(f"abilities/: must hold exactly {[a.value for a in Ability]}")

    for folder, by_id in records.items():
        for record in by_id.values():
            for target, ref in _references(record):
                if ref not in records[target]:
                    errors.append(f"{folder}/{record.id}.json: no {target} record {ref!r}")

    if errors:
        raise DataError(f"{len(errors)} problem(s) in {data_dir}:\n" + "\n".join(errors))
    return GameData(**records)  # pyright: ignore[reportArgumentType]


def _references(model: BaseModel) -> Iterator[tuple[str, str]]:
    """Every (folder, id) that `model` refers to, found through `Ref` markers in its fields."""
    for name, field in type(model).model_fields.items():
        value = getattr(model, name)
        for marker in field.metadata:
            if isinstance(marker, Ref):
                yield marker.folder, value
        yield from _references_in(field.annotation, value)


def _references_in(annotation: object, value: object) -> Iterator[tuple[str, str]]:
    if value is None:
        return
    if isinstance(value, BaseModel):
        yield from _references(value)
        return
    origin, args = get_origin(annotation), get_args(annotation)
    if origin is Annotated:
        for marker in args[1:]:
            if isinstance(marker, Ref):
                yield marker.folder, str(value)
        yield from _references_in(args[0], value)
    elif origin in (Union, UnionType):
        for arg in args:
            if arg is not NoneType:
                yield from _references_in(arg, value)
    elif origin is list and isinstance(value, list):
        for item in value:
            yield from _references_in(args[0], item)
    elif origin is dict and isinstance(value, dict):
        for key, item in value.items():
            yield from _references_in(args[0], key)
            yield from _references_in(args[1], item)

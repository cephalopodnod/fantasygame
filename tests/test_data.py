import json
import shutil
from dataclasses import fields
from pathlib import Path

import pytest
from pydantic import ValidationError

from fantasygame.content.data import DATA_DIR, DataError, GameData, load_game_data
from fantasygame.content.schemas import (
    RECORD_TYPES,
    WINDOWS_RESERVED_NAMES,
    Ability,
    Skill,
    Source,
)


@pytest.fixture
def data_copy(tmp_path: Path) -> Path:
    """A copy of data/ that a test may break."""
    return Path(shutil.copytree(DATA_DIR, tmp_path / "data"))


def write(path: Path, record: dict) -> None:
    path.write_text(json.dumps(record), encoding="utf-8")


def test_game_data_loads_with_the_whole_srd_core() -> None:
    data = load_game_data()
    assert len(data.abilities) == 6
    assert len(data.skills) == 18
    assert len(data.races) == 9
    assert len(data.classes) == 12
    assert [s.id for s in data.subraces_of("dwarf")] == ["hill-dwarf"]


def test_every_record_type_requires_a_source() -> None:
    for folder, model in RECORD_TYPES.items():
        field = model.model_fields["source"]
        assert field.is_required(), f"{folder}: source must be required"


def test_every_data_file_names_a_known_source() -> None:
    sources = {s.value for s in Source}
    for path in DATA_DIR.rglob("*.json"):
        assert json.loads(path.read_text(encoding="utf-8")).get("source") in sources, path


def test_game_data_has_a_field_for_every_record_type() -> None:
    assert [f.name for f in fields(GameData)] == list(RECORD_TYPES)


def test_record_without_a_source_is_rejected(data_copy: Path) -> None:
    juggling = {"id": "juggling", "name": "Juggling", "ability": "dexterity"}
    write(data_copy / "skills" / "juggling.json", juggling)
    with pytest.raises(DataError, match=r"skills/juggling.json(.|\n)*source"):
        load_game_data(data_copy)


def test_reference_to_a_missing_record_is_reported(data_copy: Path) -> None:
    path = data_copy / "races" / "dwarf.json"
    dwarf = json.loads(path.read_text(encoding="utf-8"))
    dwarf["traits"].append("flight")
    write(path, dwarf)
    with pytest.raises(DataError, match="races/dwarf.json: no traits record 'flight'"):
        load_game_data(data_copy)


def test_reference_inside_a_choice_is_checked(data_copy: Path) -> None:
    path = data_copy / "classes" / "fighter.json"
    fighter = json.loads(path.read_text(encoding="utf-8"))
    fighter["grants"]["choices"][0]["options"].append("juggling")
    write(path, fighter)
    with pytest.raises(DataError, match="no skills record 'juggling'"):
        load_game_data(data_copy)


def test_file_name_must_match_id(data_copy: Path) -> None:
    (data_copy / "skills" / "stealth.json").rename(data_copy / "skills" / "sneaking.json")
    with pytest.raises(DataError, match="does not match the file name"):
        load_game_data(data_copy)


def test_misspelt_field_is_rejected(data_copy: Path) -> None:
    path = data_copy / "classes" / "wizard.json"
    wizard = json.loads(path.read_text(encoding="utf-8"))
    wizard["hitdie"] = wizard.pop("hit_die")
    write(path, wizard)
    with pytest.raises(DataError, match="classes/wizard.json"):
        load_game_data(data_copy)


def test_unknown_folder_is_rejected(data_copy: Path) -> None:
    (data_copy / "clases").mkdir()
    with pytest.raises(DataError, match="clases/: unknown data folder"):
        load_game_data(data_copy)


def test_all_problems_are_reported_together(data_copy: Path) -> None:
    (data_copy / "clases").mkdir()
    (data_copy / "skills" / "broken.json").write_text("{", encoding="utf-8")
    with pytest.raises(DataError, match="^2 problem"):
        load_game_data(data_copy)


@pytest.mark.parametrize("name", ["con", "nul", "com1"])
def test_windows_reserved_names_are_not_valid_ids(name: str) -> None:
    assert name in WINDOWS_RESERVED_NAMES
    with pytest.raises(ValidationError, match="reserved by Windows"):
        Skill(id=name, name="X", source=Source.ORIGINAL, ability=Ability.DEX)

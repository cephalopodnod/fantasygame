import json
from pathlib import Path

import pytest

from fantasygame.content.manifest import load_manifest


def test_every_model_in_the_manifest_exists_and_is_licensed() -> None:
    manifest = load_manifest()
    assert manifest.models
    for entry in manifest.models.values():
        assert entry.path.is_file(), f"{entry.id}: missing file {entry.path}"
        assert entry.license and entry.author


def test_unknown_model_id_names_the_id() -> None:
    with pytest.raises(KeyError, match="no.such.model"):
        load_manifest().model("no.such.model")


def test_model_without_a_license_is_rejected(tmp_path: Path) -> None:
    manifest = {"version": 1, "models": {"m": {"path": "m.glb", "author": "someone"}}}
    (tmp_path / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(ValueError, match="license"):
        load_manifest(tmp_path)

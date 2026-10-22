"""The asset manifest: every model is referenced by an ID, never by its file path.

Swapping a placeholder for final art means changing one entry in `assets/manifest.json`
(plan choice #7). Conventions: 1 unit = 1 metre, Z up, characters face +Y after `heading`.
"""

import json
from dataclasses import dataclass
from pathlib import Path

# src/fantasygame/content/manifest.py -> repo root. Packaged builds (Phase 0, piece 4) will
# need their own lookup.
ASSETS_DIR = Path(__file__).resolve().parents[3] / "assets"
MANIFEST_VERSION = 1


@dataclass(frozen=True)
class ModelEntry:
    id: str
    path: Path
    """Absolute path to the model file."""
    scale: float
    heading: float
    """Degrees to turn the model so it faces +Y."""
    hidden_parts: tuple[str, ...]
    """Named sub-meshes to hide, e.g. spare weapons bundled with a character."""
    author: str
    license: str


@dataclass(frozen=True)
class AssetManifest:
    models: dict[str, ModelEntry]

    def model(self, model_id: str) -> ModelEntry:
        try:
            return self.models[model_id]
        except KeyError:
            raise KeyError(f"No model {model_id!r} in the asset manifest") from None


def load_manifest(assets_dir: Path = ASSETS_DIR) -> AssetManifest:
    raw = json.loads((assets_dir / "manifest.json").read_text(encoding="utf-8"))
    if raw.get("version") != MANIFEST_VERSION:
        raise ValueError(f"Unsupported asset manifest version: {raw.get('version')!r}")

    models: dict[str, ModelEntry] = {}
    for model_id, entry in raw["models"].items():
        for field in ("path", "author", "license"):
            if not entry.get(field):
                raise ValueError(f"Model {model_id!r} is missing {field!r}")
        models[model_id] = ModelEntry(
            id=model_id,
            path=assets_dir / entry["path"],
            scale=float(entry.get("scale", 1.0)),
            heading=float(entry.get("heading", 0.0)),
            hidden_parts=tuple(entry.get("hidden_parts", [])),
            author=entry["author"],
            license=entry["license"],
        )
    return AssetManifest(models)

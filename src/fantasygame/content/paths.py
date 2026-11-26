"""Where the game's folders (assets/, data/) are, whether running from the repo or the .exe."""

import sys
from pathlib import Path


def install_dir() -> Path:
    if getattr(sys, "frozen", False):  # packaged .exe: assets/ and data/ sit next to it
        return Path(sys.executable).resolve().parent
    # Running from the repo: src/fantasygame/content/paths.py -> repo root.
    return Path(__file__).resolve().parents[3]

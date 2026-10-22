"""Enforces plan choice #1: game logic never imports the engine.

Only fantasygame.client may import Panda3D (top-level modules `panda3d` and `direct`).
"""

import ast
from pathlib import Path

import pytest

PACKAGE_DIR = Path(__file__).parent.parent / "src" / "fantasygame"
ENGINE_FREE = ["content", "rules", "sim", "host", "net"]
ENGINE_MODULES = {"panda3d", "direct"}


def imported_top_level_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            modules.add(node.module.split(".")[0])
    return modules


@pytest.mark.parametrize("package", ENGINE_FREE)
def test_package_does_not_import_engine(package: str) -> None:
    offenders: dict[str, list[str]] = {}
    for path in (PACKAGE_DIR / package).rglob("*.py"):
        engine_imports = imported_top_level_modules(path) & ENGINE_MODULES
        if engine_imports:
            offenders[str(path.relative_to(PACKAGE_DIR))] = sorted(engine_imports)
    assert not offenders, f"Engine imports outside fantasygame.client: {offenders}"

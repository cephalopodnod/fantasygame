# Status — where we left off

_Read this first when picking the project back up. Updated at the end of every working session._

**Last updated:** 2026-10-21
**Current phase:** Phase 0 — Foundation and learning ([PROJECT_PLAN.md §7](PROJECT_PLAN.md#7-phases))
**Branch:** `master`

## Next step

**Finish piece 4:** the user copies `build\win_amd64\` to their second PC and runs `fantasygame.exe` (Phase 0's "done when"). Also check the first GitHub Actions run went green, and try one hand-started `.exe` build there.

Then: **Phase 1 — Rules engine** ([PROJECT_PLAN.md §7](PROJECT_PLAN.md#7-phases)). Open questions for its first piece go here once Phase 0 is closed.

## Phase 0 progress

| Piece | What | State |
|---|---|---|
| 1 | Project setup: `pyproject.toml`, uv, package layout, tests, ruff, pyright, `.gitignore`, `.gitattributes` | Done |
| 2 | Docs: [vision.md](vision.md), [house-rules.md](house-rules.md), [story/jester.md](story/jester.md), README | Done |
| 3 | First Panda3D scene (hex floor, camera, placeholder character) | Done |
| 4 | Windows build + GitHub Actions CI | Built, **awaiting test on second PC** |
| — | Learning Panda3D basics in a `sandbox/` folder | Alongside 3–4 |

## Last session (2026-10-21)

- Reviewed the old prototype and moved it to `legacy/`.
- Wrote the project plan and settled the big decisions (2014 SRD rules, Panda3D, BG3-style hex combat, co-op + solo, Steam release, unique dice rolls).
- Set up the project (piece 1) and the design documents (piece 2).
- Settled house rules: 5 difficulty levels with 5 − difficulty short rests per long rest; the spirit-fight "Restless" debuff (one ineffective short rest per stack, removed by a cleansing task); the main-stat curse hits the stat that matters most for damage and is locked at the first curse; spawned children give no XP or loot (anti-farming); ability scores follow the 2014 set levels.

## This session (2026-10-21, piece 3)

- Reviewed by the user: display looks good. `run_game.bat` added for double-click testing.
- Built the test scene: `sim/hexgrid.py` (hex maths, engine-free), `content/manifest.py` + `assets/manifest.json` (models by ID), `client/` (hex floor mesh, BG3-style camera, scene). `python -m fantasygame --screenshot FILE` renders offscreen for checks.
- Placeholder character: KayKit Knight (CC0, 76 animations) in `assets/models/characters/kaykit_knight/`. Its spare weapons are hidden through the manifest.
- Decisions (recorded in [PROJECT_PLAN.md §8](PROJECT_PLAN.md#8-placeholder-art-plan)): **pointy-top hexes** in axial coordinates; one height level = 2.5 ft (provisional); BG3-style camera controls.

## This session (2026-10-21, piece 4)

- `build_exe.bat` + `setup.py` (Panda3D `build_apps`) build `build\win_amd64\fantasygame.exe` (~76 MB folder). Tested here from another folder with no Python on PATH: renders the same as the dev version.
- The game finds `assets/` next to the `.exe` when packaged; models load through `gltf.load_model` (plugin lookup doesn't work when packaged).
- `.github/workflows/ci.yml`: checks on every push; the `.exe` build only on "Run workflow" with "Build the Windows .exe" ticked (user's choice).

## Open questions

None of these block finishing Phase 0.

**Piece 3**
- Height level of 2.5 ft (0.762 m) is provisional — revisit with the climbing/falling/jumping rules in Phase 2.

**Vision** ([vision.md §13](vision.md#13-open-questions))
- Q1 — "Expansion" and "Story" in the New Game menu: campaigns or DLC?
- Q2 — What else changes between the 5 difficulty levels?
- Q3 — What are the specialty realms?
- Q4 — Death outside spirit fights: revival, permanent, or a difficulty setting?
- Q5 — Can the roster of 10 mix player heroes and pre-built allies freely?

**House rules** ([house-rules.md](house-rules.md))
- Restless debuff: does one cleansing task remove all stacks or one? Cap stacks at 4? In-game name?
- Numbers still needed: battle reinforcements, low-man bonus, XP sources, level-gap falloff, XP table, item level requirements, crafting.

**Project**
- Game name and world name (needed before the Steam page).
- Painting 5 (The Alembic) — planned, not yet written.

## Housekeeping

- Editor: VS Code. Pick `.venv\Scripts\python.exe` as the interpreter (Ctrl+Shift+P → "Python: Select Interpreter"). The old PyCharm setup note no longer applies.
- `uv` is installed in `%USERPROFILE%\.local\bin` on each machine; after cloning, run `uv sync` once.

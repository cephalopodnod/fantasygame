# Status — where we left off

_Read this first when picking the project back up. Updated at the end of every working session._

**Last updated:** 2026-10-21
**Current phase:** Phase 0 — Foundation and learning ([PROJECT_PLAN.md §7](PROJECT_PLAN.md#7-phases))
**Branch:** `master`

## Next step

**Phase 0, piece 3 — first Panda3D scene:** a hex-grid floor with height, a camera that rotates and zooms, and one placeholder glTF character with PBR lighting, opened by `uv run python -m fantasygame`.

After that: piece 4 — package the scene into a Windows `.exe` with Panda3D's `build_apps`, and set up GitHub Actions to run the checks on every push.

## Phase 0 progress

| Piece | What | State |
|---|---|---|
| 1 | Project setup: `pyproject.toml`, uv, package layout, tests, ruff, pyright, `.gitignore`, `.gitattributes` | Done |
| 2 | Docs: [vision.md](vision.md), [house-rules.md](house-rules.md), [story/jester.md](story/jester.md), README | Done |
| 3 | First Panda3D scene (hex floor, camera, placeholder character) | **Next** |
| 4 | Windows build + GitHub Actions CI | To do |
| — | Learning Panda3D basics in a `sandbox/` folder | Alongside 3–4 |

## Last session (2026-10-21)

- Reviewed the old prototype and moved it to `legacy/`.
- Wrote the project plan and settled the big decisions (2014 SRD rules, Panda3D, BG3-style hex combat, co-op + solo, Steam release, unique dice rolls).
- Set up the project (piece 1) and the design documents (piece 2).
- Settled house rules: 5 difficulty levels with 5 − difficulty short rests per long rest; the spirit-fight "Restless" debuff (one ineffective short rest per stack, removed by a cleansing task); the main-stat curse hits the stat that matters most for damage and is locked at the first curse; spawned children give no XP or loot (anti-farming); ability scores follow the 2014 set levels.

## Open questions

None of these block piece 3.

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

- PyCharm: open the repo root, use `.venv\Scripts\python.exe` as the interpreter, mark `src` as Sources Root and `tests` as Test Sources Root. (Not yet confirmed done.)
- `uv` is installed in `C:\Users\timot\.local\bin`; restart terminals so it's on PATH.

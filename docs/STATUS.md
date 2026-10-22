# Status — where we left off

_Read this first when picking the project back up. Updated at the end of every working session._

**Last updated:** 2026-10-21
**Current phase:** Phase 1 — Rules engine ([PROJECT_PLAN.md §7](PROJECT_PLAN.md#7-phases))
**Branch:** `master`

## Next step

**Phase 1, piece 2 — data foundation:** `data/` folder, pydantic schemas, the `source` field and its test, and the SRD import tool.

Still open from Phase 0: run `build\win_amd64\fantasygame.exe` on the user's second PC (Phase 0's "done when"). Doesn't block Phase 1.

## Phase 1 progress

| Piece | What | State |
|---|---|---|
| 1 | Dice service: expressions, advantage, fresh randomness, roll log, fixed dice for tests/replay | Done |
| 2 | Data foundation: `data/`, schemas, `source` field, SRD import tool | **Next** |
| 3 | Abilities, proficiency, skills, checks and saves | To do |
| 4 | Features and effects system (plan choice #4) | To do |
| 5 | Races, backgrounds, classes, character creation (point-buy, standard array, 4d6) | To do |
| 6 | Levelling: rolled HP, hit dice, spell slots incl. pact magic and multiclass, rests, conditions | To do |
| 7 | Skill-tree format + one sample tree | To do |
| 8 | "Done when": level 1/5/10 characters of all 12 classes match the SRD | To do |

## This session (2026-10-21)

- **Phase 0, pieces 3–4:** hex test scene (pointy-top hexes, BG3-style camera, KayKit Knight placeholder), `run_game.bat`, Windows build (`build_exe.bat`, ~76 MB folder, tested here without Python), GitHub Actions CI (checks on every push; `.exe` build by hand). All merged into `master`; CI green.
- **Phase 1 decisions** (in [house-rules.md](house-rules.md)): HP on level-up is **rolled**; ability scores by **point-buy, standard array or 4d6 drop lowest**; **multiclassing** per the 2014 rules (code from Phase 1, UI later).
- **Piece 1:** `rules/dice.py` — `Dice` with `roll("2d6+3")`, `"4d6kh3"`, and `d20(Advantage...)`; `SystemRandomSource` (OS randomness, nothing to save) and `FixedSequenceSource` (tests and replay). Every result keeps its raw faces and reason; listeners (later the session log) see every roll.

## Open questions

None of these block piece 2.

**Phase 1**
- Rolled HP and 4d6 can be re-rolled by reloading a save (a side effect of unique dice). Accepted for now — revisit if it feels exploitable.

**Earlier**
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

- Editor: VS Code. Pick `.venv\Scripts\python.exe` as the interpreter (Ctrl+Shift+P → "Python: Select Interpreter").
- `uv` is installed in `%USERPROFILE%\.local\bin` on each machine; after cloning, run `uv sync` once.
- Build the game: `build_exe.bat`. Its log on a player's PC: `%LOCALAPPDATA%\fantasygame\output.log`.

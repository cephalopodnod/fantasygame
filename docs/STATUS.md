# Status — where we left off

_Read this first when picking the project back up. Updated at the end of every working session._

**Last updated:** 2026-11-24
**Current phase:** Phase 1 — Rules engine ([PROJECT_PLAN.md §7](PROJECT_PLAN.md#7-phases))
**Branch:** `master`

## Next step

**Phase 1, piece 3 — abilities, proficiency, skills, checks and saves** (in `rules/`, using the dice service and the new data).

Still open from Phase 0: run `build\win_amd64\fantasygame.exe` on the user's second PC (Phase 0's "done when"). Doesn't block Phase 1.

## Phase 1 progress

| Piece | What | State |
|---|---|---|
| 1 | Dice service: expressions, advantage, fresh randomness, roll log, fixed dice for tests/replay | Done |
| 2 | Data foundation: `data/`, schemas, `source` field, SRD import tool | Done |
| 3 | Abilities, proficiency, skills, checks and saves | **Next** |
| 4 | Features and effects system (plan choice #4) | To do |
| 5 | Races, backgrounds, classes, character creation (point-buy, standard array, 4d6) | To do |
| 6 | Levelling: rolled HP, hit dice, spell slots incl. pact magic and multiclass, rests, conditions | To do |
| 7 | Skill-tree format + one sample tree | To do |
| 8 | "Done when": level 1/5/10 characters of all 12 classes match the SRD | To do |

## This session (2026-11-24)

- **Piece 2:** `content/schemas.py` (pydantic record types), `content/data.py` (loads `data/`, checks schemas, file names and references, reports all problems at once), `tools/srd_import.py` (2014 endpoints of the D&D 5e API → our format). 197 SRD records imported: abilities, skills, languages, proficiencies, racial traits, races, subraces, backgrounds, classes (core fields). Checked by hand against the SRD class and race tables. `data/` ships with the `.exe`.
- **Decisions** (in [PROJECT_PLAN.md §8b](PROJECT_PLAN.md#8b-game-data)): our own data format, one record per file, `source` is `srd-5.1` or `original`, imported JSON is committed, SRD credit in `data/ATTRIBUTION.md`.

**Previous session (2026-10-21):** Phase 0 finished (hex scene, Windows build, CI); Phase 1 piece 1 (dice service); HP rolled, point-buy/standard array/4d6, 2014 multiclassing.

## Open questions

None of these block piece 3.

**Phase 1**
- The SRD has only one background (Acolyte), one subclass per class and one feat. We'll need original backgrounds before character creation feels complete — how many, and which?
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

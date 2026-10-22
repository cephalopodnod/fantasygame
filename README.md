# fantasygame (working title)

A co-op fantasy RPG with real-time exploration and turn-based hex-grid combat, built on the 2014 SRD 5.1 rules with original subclasses and skill trees. Written in Python with Panda3D. Early development.

## Documents

| Document | What's in it |
|---|---|
| [docs/STATUS.md](docs/STATUS.md) | Where we left off and what's next |
| [docs/vision.md](docs/vision.md) | What the game is: world, story, party, progression, combat |
| [docs/PROJECT_PLAN.md](docs/PROJECT_PLAN.md) | Decisions, architecture and the phased roadmap |
| [docs/house-rules.md](docs/house-rules.md) | Where the game differs from the 2014 rules |
| [docs/story/jester.md](docs/story/jester.md) | The Jester and the six Houses |

## Getting started (Windows)

1. Install [uv](https://docs.astral.sh/uv/):
   ```
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
2. From the repo folder, install everything (creates `.venv/`):
   ```
   uv sync
   ```
3. Run the game (or double-click `run_game.bat`):
   ```
   uv run python -m fantasygame
   ```

## Building the Windows game

Double-click `build_exe.bat` (or run it in a terminal). The game lands in `build\win_amd64\`; copy that whole folder to any Windows PC and run `fantasygame.exe` — no Python needed. The game's log file is `%LOCALAPPDATA%\fantasygame\output.log`.

GitHub can build it too: **Actions → CI → Run workflow**, tick **Build the Windows .exe**, then download `fantasygame-windows` from the finished run. Every push runs the checks (tests, lint, type check) automatically.

## Development commands

| Command | What it does |
|---|---|
| `uv run pytest` | Run the tests |
| `uv run ruff check` | Lint |
| `uv run ruff format` | Format the code |
| `uv run pyright` | Type check |
| `uv add <package>` | Add a dependency |

## Repository layout

```
src/fantasygame/   the game
  content/         loading and checking game data
  rules/           2014 SRD rules + house rules
  sim/             game state and simulation
  host/            authoritative host (also runs solo games)
  net/             connections: in-process, direct IP, later Steam
  client/          Panda3D rendering, input, UI (only part allowed to use Panda3D)
tests/             automated tests
docs/              design documents
legacy/            the original prototype, kept for reference
```

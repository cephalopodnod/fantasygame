# CLAUDE.md

## Start of every session

1. Read `docs/STATUS.md` first.
2. Give a short summary of where we left off and what's next.
3. Ask the open questions that matter for the next step before starting work.

## End of every session (or after each finished piece)

Update `docs/STATUS.md`: last-updated date, current phase and piece, next step, what was done, decisions made, and open questions. Keep it short — it's a pointer, not a log of everything.

## How we work

- Work through tasks **one piece at a time**. Finish, check and review each piece with the user before moving on.
- The user has minimal game-programming experience and wants to build for the long term. Explain choices plainly and say why, especially when they are hard to change later.
- Record decisions in the docs, not just in chat: game design in `docs/vision.md`, rule changes in `docs/house-rules.md`, technical decisions in `docs/PROJECT_PLAN.md`.

## Key documents

- `docs/STATUS.md` — where we left off
- `docs/PROJECT_PLAN.md` — decisions, architecture, phases (§3 lists the choices that must not be broken)
- `docs/vision.md` — what the game is
- `docs/house-rules.md` — differences from the 2014 rules
- `docs/story/jester.md` — the Jester storyline
- `legacy/` — the old prototype; reference only, never imported or fixed

## Rules that must hold

- Only `fantasygame.client` may import Panda3D (`panda3d`, `direct`). `tests/test_architecture.py` enforces this.
- Rules content is 2014 **SRD 5.1** only; everything else is original. Every data record carries a `source` field.
- All dice rolls go through the host's dice service with fresh randomness; dice state is never saved.
- Game logic changes happen through commands and events (needed for co-op).

## Commands

`uv` lives in `C:\Users\timot\.local\bin` (add to PATH in the shell if `uv` isn't found).

```
uv run python -m fantasygame   # run
uv run pytest                  # tests
uv run ruff check              # lint
uv run ruff format             # format
uv run pyright                 # type check
```

Run tests, ruff (check + format --check) and pyright before every commit.

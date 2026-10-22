"""Entry point: `python -m fantasygame` or the `fantasygame` command."""

import argparse
from pathlib import Path

from fantasygame import __version__


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="fantasygame")
    parser.add_argument("--version", action="version", version=f"fantasygame {__version__}")
    parser.add_argument(
        "--screenshot",
        type=Path,
        metavar="FILE",
        help="render the scene offscreen, save it as an image and quit (for checks, bug reports)",
    )
    args = parser.parse_args(argv)

    # Imported here so `--version` and the tests don't need to load the 3D engine.
    from fantasygame.client.app import run

    run(screenshot=args.screenshot)


if __name__ == "__main__":
    main()

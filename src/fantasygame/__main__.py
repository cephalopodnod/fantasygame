"""Entry point: `python -m fantasygame` or the `fantasygame` command."""

from fantasygame import __version__


def main() -> None:
    print(f"fantasygame {__version__}")


if __name__ == "__main__":
    main()

import fantasygame
from fantasygame.__main__ import main


def test_version_is_set() -> None:
    assert fantasygame.__version__


def test_main_prints_version(capsys) -> None:
    main()
    assert fantasygame.__version__ in capsys.readouterr().out

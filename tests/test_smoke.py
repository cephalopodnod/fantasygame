import pytest

import fantasygame
from fantasygame.__main__ import main


def test_version_is_set() -> None:
    assert fantasygame.__version__


def test_version_flag_prints_version(capsys) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])
    assert exit_info.value.code == 0
    assert fantasygame.__version__ in capsys.readouterr().out

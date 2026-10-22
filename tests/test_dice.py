from collections import Counter

import pytest

from fantasygame.rules.dice import (
    Advantage,
    D20Result,
    Dice,
    DiceError,
    FixedSequenceSource,
    RollResult,
    SystemRandomSource,
    parse,
)


def fixed(*faces: int) -> Dice:
    return Dice(FixedSequenceSource(faces))


# --- Parsing ---


@pytest.mark.parametrize(
    ("text", "normalised"),
    [
        ("1d8", "1d8"),
        ("d20", "1d20"),
        ("2d6+3", "2d6+3"),
        ("2D6 + 3", "2d6+3"),
        ("1d8+1d6-1", "1d8+1d6-1"),
        ("4d6kh3", "4d6kh3"),
        ("2d20kl1", "2d20kl1"),
        ("5", "5"),
        ("-2", "-2"),
        ("1d4-1d4", "1d4-1d4"),
    ],
)
def test_parse_round_trips(text: str, normalised: str) -> None:
    assert str(parse(text)) == normalised


@pytest.mark.parametrize(
    "text",
    ["", "d", "2d", "1d1", "0d6", "101d6", "1d6kh", "2d6kh3", "1d6 3", "1d6+", "fireball", "1d6*2"],
)
def test_parse_rejects_bad_expressions(text: str) -> None:
    with pytest.raises(DiceError):
        parse(text)


# --- Rolling ---


def test_roll_adds_faces_and_modifier() -> None:
    result = fixed(4, 6).roll("2d6+3", reason="Greatsword")
    assert result.total == 13
    assert result.faces == (4, 6)
    assert result.reason == "Greatsword"


def test_subtracted_term() -> None:
    assert fixed(5, 2).roll("1d6-1d4").total == 3


def test_keep_highest_drops_the_lowest() -> None:
    result = fixed(3, 1, 6, 4).roll("4d6kh3")
    assert result.total == 13
    assert result.faces == (3, 1, 6, 4)
    assert sorted(result.terms[0].kept) == [3, 4, 6]


def test_keep_lowest() -> None:
    assert fixed(15, 7).roll("2d20kl1").total == 7


def test_replaying_the_faces_reproduces_the_roll() -> None:
    original = Dice().roll("4d6kh3+1d8-2")
    replay = fixed(*original.faces).roll("4d6kh3+1d8-2")
    assert replay == original


# --- d20 and advantage ---


def test_plain_d20_uses_one_die() -> None:
    result = fixed(12).d20()
    assert result.faces == (12,)
    assert result.natural == 12


def test_advantage_takes_the_higher() -> None:
    assert fixed(5, 17).d20(Advantage.ADVANTAGE).natural == 17


def test_disadvantage_takes_the_lower() -> None:
    assert fixed(5, 17).d20(Advantage.DISADVANTAGE).natural == 5


@pytest.mark.parametrize(
    ("advantage", "disadvantage", "expected"),
    [
        (False, False, Advantage.NONE),
        (True, False, Advantage.ADVANTAGE),
        (False, True, Advantage.DISADVANTAGE),
        (True, True, Advantage.NONE),
    ],
)
def test_advantage_and_disadvantage_cancel(
    advantage: bool, disadvantage: bool, expected: Advantage
) -> None:
    assert Advantage.combine(advantage, disadvantage) is expected


def test_natural_20_and_1() -> None:
    assert fixed(20).d20().is_natural_20
    assert fixed(1).d20().is_natural_1
    assert not fixed(1, 20).d20(Advantage.ADVANTAGE).is_natural_1


# --- The randomness itself ---


def test_listeners_see_every_roll() -> None:
    seen: list[RollResult | D20Result] = []
    dice = fixed(3, 4, 18)
    dice.add_listener(seen.append)
    dice.roll("2d6")
    dice.d20()
    assert [type(r) for r in seen] == [RollResult, D20Result]


def test_fixed_source_refuses_impossible_faces_and_running_out() -> None:
    with pytest.raises(DiceError, match="impossible"):
        fixed(7).roll("1d6")
    with pytest.raises(DiceError, match="ran out"):
        fixed(3).roll("2d6")


def test_system_random_covers_every_face_and_nothing_else() -> None:
    source = SystemRandomSource()
    counts = Counter(source.roll_die(20) for _ in range(4000))
    assert set(counts) == set(range(1, 21))
    # Each face expects 200; anything under 100 would mean badly skewed dice.
    assert min(counts.values()) > 100


def test_two_dice_services_do_not_repeat_each_other() -> None:
    first = [Dice().d20().natural for _ in range(30)]
    second = [Dice().d20().natural for _ in range(30)]
    assert first != second

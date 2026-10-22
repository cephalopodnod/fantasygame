"""Dice: expressions like "2d6+3", d20 rolls with advantage, and where the randomness comes from.

Plan choice #3: only the host rolls, through one `Dice` object, and every roll uses fresh
randomness. `SystemRandomSource` draws from the operating system, so there is no dice state
that a save could capture; reloading and retrying gives a new result.

Every result keeps its raw die faces in order. The session log records them, and feeding them
back through `FixedSequenceSource` replays a fight exactly. Tests use the same source to script
the dice.
"""

import random
import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from enum import Enum
from typing import Protocol

MAX_DICE_PER_TERM = 100


class DiceError(ValueError):
    pass


# --- Where the randomness comes from ---


class RandomSource(Protocol):
    def roll_die(self, sides: int) -> int:
        """One die face, 1 to `sides`."""
        ...


class SystemRandomSource:
    """Fresh operating-system randomness; nothing to seed, nothing to save."""

    def __init__(self) -> None:
        self._random = random.SystemRandom()

    def roll_die(self, sides: int) -> int:
        return self._random.randint(1, sides)


class FixedSequenceSource:
    """Returns the given faces in order. For tests and for replaying a session log."""

    def __init__(self, faces: Iterable[int]) -> None:
        self._faces = list(faces)
        self._next = 0

    def roll_die(self, sides: int) -> int:
        if self._next >= len(self._faces):
            raise DiceError(f"Fixed dice ran out after {len(self._faces)} rolls")
        face = self._faces[self._next]
        if not 1 <= face <= sides:
            raise DiceError(f"Fixed face {face} is impossible on a d{sides}")
        self._next += 1
        return face

    @property
    def remaining(self) -> int:
        return len(self._faces) - self._next


# --- Expressions ---


@dataclass(frozen=True)
class DiceTerm:
    """`count` dice with `sides` faces, optionally keeping only the highest/lowest `keep`."""

    count: int
    sides: int
    keep: int | None = None
    keep_highest: bool = True
    sign: int = 1

    def __str__(self) -> str:
        keep = "" if self.keep is None else f"{'kh' if self.keep_highest else 'kl'}{self.keep}"
        return f"{self.count}d{self.sides}{keep}"


@dataclass(frozen=True)
class DiceExpression:
    terms: tuple[DiceTerm, ...]
    modifier: int = 0

    def __str__(self) -> str:
        parts: list[str] = []
        for term in self.terms:
            parts.append(("-" if term.sign < 0 else "+") + str(term))
        if self.modifier or not parts:
            parts.append(f"{self.modifier:+d}")
        text = "".join(parts)
        return text.removeprefix("+")


# A sign (needed between terms), then dice or a number. Spaces only around the signs.
_TOKEN = re.compile(r"\s*([+-])?\s*(?:(\d*)d(\d+)(?:(kh|kl)(\d+))?|(\d+))\s*", re.IGNORECASE)


def parse(text: str) -> DiceExpression:
    """Parse "1d8", "2d6+3", "1d8+1d6-1" or "4d6kh3" (roll 4d6, keep the highest 3)."""
    source = text.strip()
    if not source:
        raise DiceError("Empty dice expression")
    terms: list[DiceTerm] = []
    modifier = 0
    position = 0
    while position < len(source):
        match = _TOKEN.match(source, position)
        if match is None or (match.group(1) is None and position > 0):
            raise DiceError(f"Can't read dice expression {text!r}")
        sign = -1 if match.group(1) == "-" else 1
        if match.group(6) is not None:
            modifier += sign * int(match.group(6))
        else:
            count = int(match.group(2) or 1)
            sides = int(match.group(3))
            if not 1 <= count <= MAX_DICE_PER_TERM:
                raise DiceError(f"{text!r}: dice count must be 1 to {MAX_DICE_PER_TERM}")
            if sides < 2:
                raise DiceError(f"{text!r}: a die needs at least 2 sides")
            keep = int(match.group(5)) if match.group(5) else None
            if keep is not None and not 1 <= keep <= count:
                raise DiceError(f"{text!r}: can only keep 1 to {count} dice")
            keep_highest = (match.group(4) or "kh").lower() == "kh"
            terms.append(DiceTerm(count, sides, keep, keep_highest, sign))
        position = match.end()
    return DiceExpression(tuple(terms), modifier)


# --- Results ---


@dataclass(frozen=True)
class TermResult:
    term: DiceTerm
    faces: tuple[int, ...]
    """Every die rolled, in order, including dropped ones."""
    kept: tuple[int, ...]

    @property
    def total(self) -> int:
        return self.term.sign * sum(self.kept)


@dataclass(frozen=True)
class RollResult:
    expression: DiceExpression
    terms: tuple[TermResult, ...]
    reason: str
    """What the roll was for, e.g. "Goblin attack" (for the combat log and debugging)."""

    @property
    def total(self) -> int:
        return sum(t.total for t in self.terms) + self.expression.modifier

    @property
    def faces(self) -> tuple[int, ...]:
        """All raw die faces in the order rolled; replaying them reproduces this result."""
        return tuple(face for t in self.terms for face in t.faces)


class Advantage(Enum):
    NONE = "none"
    ADVANTAGE = "advantage"
    DISADVANTAGE = "disadvantage"

    @staticmethod
    def combine(advantage: bool, disadvantage: bool) -> Advantage:
        """2014 rule: having both cancels out, however many sources of each."""
        if advantage == disadvantage:
            return Advantage.NONE
        return Advantage.ADVANTAGE if advantage else Advantage.DISADVANTAGE


@dataclass(frozen=True)
class D20Result:
    faces: tuple[int, ...]
    """One face, or two with advantage/disadvantage."""
    advantage: Advantage
    reason: str

    @property
    def natural(self) -> int:
        """The face that counts."""
        if self.advantage is Advantage.ADVANTAGE:
            return max(self.faces)
        if self.advantage is Advantage.DISADVANTAGE:
            return min(self.faces)
        return self.faces[0]

    @property
    def is_natural_20(self) -> bool:
        return self.natural == 20

    @property
    def is_natural_1(self) -> bool:
        return self.natural == 1


type RollListener = Callable[[RollResult | D20Result], None]


# --- The dice service ---


class Dice:
    """All rolling goes through here. Listeners (e.g. the session log) see every result."""

    def __init__(self, source: RandomSource | None = None) -> None:
        self._source = source if source is not None else SystemRandomSource()
        self._listeners: list[RollListener] = []

    def add_listener(self, listener: RollListener) -> None:
        self._listeners.append(listener)

    def roll(self, expression: str | DiceExpression, reason: str = "") -> RollResult:
        expr = parse(expression) if isinstance(expression, str) else expression
        results: list[TermResult] = []
        for term in expr.terms:
            faces = tuple(self._source.roll_die(term.sides) for _ in range(term.count))
            if term.keep is None:
                kept = faces
            else:
                kept = tuple(sorted(faces, reverse=term.keep_highest)[: term.keep])
            results.append(TermResult(term, faces, kept))
        result = RollResult(expr, tuple(results), reason)
        self._notify(result)
        return result

    def d20(self, advantage: Advantage = Advantage.NONE, reason: str = "") -> D20Result:
        count = 1 if advantage is Advantage.NONE else 2
        faces = tuple(self._source.roll_die(20) for _ in range(count))
        result = D20Result(faces, advantage, reason)
        self._notify(result)
        return result

    def _notify(self, result: RollResult | D20Result) -> None:
        for listener in self._listeners:
            listener(result)

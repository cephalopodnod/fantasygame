"""Hex grid maths: pointy-top hexes in axial coordinates (q, r).

Follows Red Blob Games' "Hexagonal Grids" guide (redblobgames.com/grids/hexagons).
World axes match Panda3D: X right, Y forward ("north"), Z up, in metres.
`q` grows to the east; `r` grows to the north-east row by row.
"""

import math
from dataclasses import dataclass

HEX_WIDTH_M = 1.524
"""One hex is 5 ft across its flats."""
HEX_RADIUS_M = HEX_WIDTH_M / math.sqrt(3)
"""Centre to corner."""
HEIGHT_LEVEL_M = 0.762
"""One height level is 2.5 ft. Provisional: the rules for climbing and falling may change it."""


@dataclass(frozen=True, slots=True)
class Hex:
    q: int
    r: int

    @property
    def s(self) -> int:
        """Third cube coordinate; q + r + s is always 0."""
        return -self.q - self.r

    def __add__(self, other: Hex) -> Hex:
        return Hex(self.q + other.q, self.r + other.r)

    def __sub__(self, other: Hex) -> Hex:
        return Hex(self.q - other.q, self.r - other.r)

    def neighbors(self) -> list[Hex]:
        return [self + d for d in DIRECTIONS]

    def distance_to(self, other: Hex) -> int:
        d = self - other
        return max(abs(d.q), abs(d.r), abs(d.s))


DIRECTIONS = (Hex(1, 0), Hex(0, 1), Hex(-1, 1), Hex(-1, 0), Hex(0, -1), Hex(1, -1))
"""East, then anticlockwise."""


def hex_to_world(h: Hex) -> tuple[float, float]:
    """Centre of a hex on the ground plane."""
    x = HEX_RADIUS_M * math.sqrt(3) * (h.q + h.r / 2)
    y = HEX_RADIUS_M * 1.5 * h.r
    return x, y


def hex_corners(h: Hex, radius: float = HEX_RADIUS_M) -> list[tuple[float, float]]:
    """The six corners, anticlockwise from the north-east one (pointy-top: a corner faces north)."""
    cx, cy = hex_to_world(h)
    corners: list[tuple[float, float]] = []
    for i in range(6):
        angle = math.radians(30 + 60 * i)
        corners.append((cx + radius * math.cos(angle), cy + radius * math.sin(angle)))
    return corners


def hexes_in_range(center: Hex, radius: int) -> list[Hex]:
    """Every hex within `radius` steps of `center`, including it."""
    result: list[Hex] = []
    for q in range(-radius, radius + 1):
        for r in range(max(-radius, -q - radius), min(radius, -q + radius) + 1):
            result.append(center + Hex(q, r))
    return result

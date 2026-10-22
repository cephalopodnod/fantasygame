import math

import pytest

from fantasygame.sim.hexgrid import (
    DIRECTIONS,
    HEX_RADIUS_M,
    HEX_WIDTH_M,
    Hex,
    hex_corners,
    hex_to_world,
    hexes_in_range,
)


def test_cube_coordinates_sum_to_zero() -> None:
    h = Hex(3, -5)
    assert h.q + h.r + h.s == 0


def test_every_neighbor_is_one_step_and_one_hex_width_away() -> None:
    origin = Hex(2, -1)
    ox, oy = hex_to_world(origin)
    for n in origin.neighbors():
        nx, ny = hex_to_world(n)
        assert origin.distance_to(n) == 1
        assert math.dist((ox, oy), (nx, ny)) == pytest.approx(HEX_WIDTH_M)


def test_directions_go_anticlockwise_from_east() -> None:
    angles = [math.degrees(math.atan2(*reversed(hex_to_world(d)))) for d in DIRECTIONS]
    assert angles == pytest.approx([0, 60, 120, 180, -120, -60])


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (Hex(0, 0), Hex(0, 0), 0),
        (Hex(0, 0), Hex(3, 0), 3),
        (Hex(0, 0), Hex(2, -4), 4),
        (Hex(-2, 1), Hex(1, 3), 5),
    ],
)
def test_distance(a: Hex, b: Hex, expected: int) -> None:
    assert a.distance_to(b) == expected
    assert b.distance_to(a) == expected


def test_pointy_top_has_a_corner_facing_north() -> None:
    corners = hex_corners(Hex(0, 0))
    assert max(y for _, y in corners) == pytest.approx(HEX_RADIUS_M)
    assert any(x == pytest.approx(0) and y > 0 for x, y in corners)


@pytest.mark.parametrize("radius", [0, 1, 2, 7])
def test_hexes_in_range(radius: int) -> None:
    center = Hex(1, -2)
    hexes = hexes_in_range(center, radius)
    assert len(hexes) == 3 * radius * (radius + 1) + 1
    assert len(set(hexes)) == len(hexes)
    assert all(center.distance_to(h) <= radius for h in hexes)

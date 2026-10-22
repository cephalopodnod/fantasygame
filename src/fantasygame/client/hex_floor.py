"""Builds the hex floor as a single mesh: one six-sided column per hex, raised by its height."""

from collections.abc import Mapping

from panda3d.core import (
    Geom,
    GeomNode,
    GeomTriangles,
    GeomVertexData,
    GeomVertexFormat,
    GeomVertexWriter,
    Material,
    NodePath,
)

from fantasygame.sim.hexgrid import HEIGHT_LEVEL_M, HEX_RADIUS_M, Hex, hex_corners, hex_to_world

TOP_INSET = 0.95
"""Tops are drawn slightly smaller than the hex so the grid shows as thin dark gaps."""
FLOOR_BOTTOM_Z = -0.3

type Color = tuple[float, float, float, float]
"""sRGB, as picked in a paint program; converted to linear for the PBR lighting."""

GRASS_BY_LEVEL: tuple[Color, ...] = (
    (0.30, 0.45, 0.22, 1.0),
    (0.38, 0.50, 0.25, 1.0),
    (0.50, 0.52, 0.34, 1.0),
    (0.58, 0.56, 0.48, 1.0),
)
CLIFF: Color = (0.36, 0.30, 0.24, 1.0)
GAP: Color = (0.10, 0.09, 0.08, 1.0)


def make_hex_floor(heights: Mapping[Hex, int]) -> NodePath:
    """One mesh for the whole floor; `heights` maps each hex to its height level."""
    data = GeomVertexData("hex-floor", GeomVertexFormat.get_v3n3c4(), Geom.UH_static)
    position = GeomVertexWriter(data, "vertex")
    normal = GeomVertexWriter(data, "normal")
    color = GeomVertexWriter(data, "color")
    triangles = GeomTriangles(Geom.UH_static)
    count = 0

    def vertex(x: float, y: float, z: float, n: tuple[float, float, float], c: Color) -> int:
        nonlocal count
        position.add_data3(x, y, z)
        normal.add_data3(*n)
        color.add_data4(*_to_linear(c))
        count += 1
        return count - 1

    for h, level in heights.items():
        top_z = level * HEIGHT_LEVEL_M
        top_color = _shade(GRASS_BY_LEVEL[min(level, len(GRASS_BY_LEVEL) - 1)], h)
        corners = hex_corners(h, HEX_RADIUS_M * TOP_INSET)
        cx, cy = hex_to_world(h)

        # Base: a dark full-size hex under everything, seen through the gaps between tops.
        up = (0.0, 0.0, 1.0)
        base = [vertex(x, y, FLOOR_BOTTOM_Z, up, GAP) for x, y in hex_corners(h)]
        for i in range(1, 5):
            triangles.add_vertices(base[0], base[i], base[i + 1])

        # Top: a fan of six triangles around the centre.
        centre = vertex(cx, cy, top_z, up, top_color)
        rim = [vertex(x, y, top_z, up, top_color) for x, y in corners]
        for i in range(6):
            triangles.add_vertices(centre, rim[i], rim[(i + 1) % 6])

        # Sides: one outward-facing quad per edge, down to the bottom of the floor.
        for i in range(6):
            (x1, y1), (x2, y2) = corners[i], corners[(i + 1) % 6]
            mx, my = (x1 + x2) / 2 - cx, (y1 + y2) / 2 - cy
            length = (mx * mx + my * my) ** 0.5
            side_normal = (mx / length, my / length, 0.0)
            a = vertex(x1, y1, top_z, side_normal, CLIFF)
            b = vertex(x2, y2, top_z, side_normal, CLIFF)
            c = vertex(x2, y2, FLOOR_BOTTOM_Z, side_normal, CLIFF)
            d = vertex(x1, y1, FLOOR_BOTTOM_Z, side_normal, CLIFF)
            triangles.add_vertices(a, c, b)
            triangles.add_vertices(a, d, c)

    geom = Geom(data)
    geom.add_primitive(triangles)
    node = GeomNode("hex-floor")
    node.add_geom(geom)
    floor = NodePath(node)

    material = Material("hex-floor")
    material.set_base_color((1, 1, 1, 1))  # the vertex colours carry the actual colour
    material.set_roughness(0.9)
    material.set_metallic(0.0)
    floor.set_material(material)
    return floor


def _shade(c: Color, h: Hex) -> Color:
    """Tiny brightness variation per hex so neighbouring tops are easy to tell apart."""
    factor = (0.94, 1.0, 1.06)[(h.q - h.r) % 3]
    return (c[0] * factor, c[1] * factor, c[2] * factor, c[3])


def _to_linear(c: Color) -> Color:
    def channel(v: float) -> float:
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4

    return (channel(c[0]), channel(c[1]), channel(c[2]), c[3])

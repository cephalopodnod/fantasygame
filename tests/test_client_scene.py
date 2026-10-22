"""Builds the test scene offscreen and renders a few frames.

Needs a graphics driver; machines without one (some CI runners) skip it.
"""

from pathlib import Path

import pytest

from fantasygame.client.app import GameApp, demo_heights, run
from fantasygame.sim.hexgrid import Hex


def test_demo_map_is_a_radius_7_hex_with_heights() -> None:
    heights = demo_heights()
    assert len(heights) == 169
    assert heights[Hex(0, 0)] == 0
    assert max(heights.values()) >= 2


def test_scene_renders_and_saves_a_screenshot(tmp_path: Path) -> None:
    try:
        app = GameApp(offscreen=True)
    except Exception as error:  # no OpenGL available
        pytest.skip(f"No graphics available: {error}")
    try:
        assert not app.floor.is_empty()
        assert "Idle" in app.actor.get_anim_names()
        assert app.actor.find("**/2H_Sword").is_empty()  # spare weapons were removed
    finally:
        app.destroy()

    screenshot = tmp_path / "scene.png"
    run(screenshot=screenshot)
    assert screenshot.stat().st_size > 0

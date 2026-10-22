"""The game window. For now: the Phase 0 test scene (hex floor, camera, one character)."""

from pathlib import Path

import simplepbr
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBase import ShowBase
from panda3d.core import (
    AmbientLight,
    DirectionalLight,
    Filename,
    NodePath,
    Point3,
    TextNode,
    load_prc_file_data,
)

from fantasygame import __version__
from fantasygame.client.camera import CameraRig
from fantasygame.client.hex_floor import make_hex_floor
from fantasygame.client.models import load_actor
from fantasygame.content.manifest import load_manifest
from fantasygame.sim.hexgrid import HEIGHT_LEVEL_M, Hex, hex_to_world, hexes_in_range

SKY = (0.55, 0.70, 0.85, 1.0)
CONTROLS = "WASD / arrows: move   Q/E or middle-drag: rotate   Wheel: zoom   Esc: quit"


def demo_heights() -> dict[Hex, int]:
    """A small test map: flat ground, a hill to the north-west, and a ledge with a ramp."""
    heights: dict[Hex, int] = {}
    hill = Hex(-4, 5)
    for h in hexes_in_range(Hex(0, 0), 7):
        level = max(0, 3 - h.distance_to(hill))
        if h.q >= 4:
            level = max(level, 2)
        elif h.q == 3 and h.r <= -1:
            level = max(level, 1)  # the ramp up to the ledge
        heights[h] = level
    return heights


class GameApp(ShowBase):
    def __init__(self, offscreen: bool = False) -> None:
        load_prc_file_data(
            "",
            f"""
            window-title fantasygame {__version__}
            win-size 1280 720
            sync-video true
            show-frame-rate-meter {"false" if offscreen else "true"}
            {"window-type offscreen" if offscreen else ""}
            """,
        )
        super().__init__()
        simplepbr.init(enable_shadows=True, use_normal_maps=False, msaa_samples=4)
        self.set_background_color(*SKY)
        self.accept("escape", self.userExit)

        heights = demo_heights()
        self.floor = make_hex_floor(heights)
        self.floor.reparent_to(self.render)
        self._add_lights()

        start = Hex(0, 0)
        x, y = hex_to_world(start)
        self.character: NodePath = self.render.attach_new_node("character")
        self.character.set_pos(x, y, heights[start] * HEIGHT_LEVEL_M)
        self.character.set_h(-20)  # turned a little towards the camera
        actor = load_actor(load_manifest().model("placeholder.knight"))
        actor.reparent_to(self.character)
        actor.loop("Idle")
        self.actor = actor

        self.camera_rig = CameraRig(self, focus=Point3(x, y, 0.5), yaw=200)
        if not offscreen:
            OnscreenText(
                text=CONTROLS,
                parent=self.a2dBottomLeft,
                pos=(0.05, 0.05),
                scale=0.045,
                align=TextNode.A_left,
                fg=(1, 1, 1, 1),
                shadow=(0, 0, 0, 0.8),
            )

    def _add_lights(self) -> None:
        sun = DirectionalLight("sun")
        sun.set_color((2.2, 2.1, 1.95, 1))
        sun.set_shadow_caster(True, 2048, 2048)
        lens = sun.get_lens()
        lens.set_film_size(26, 26)
        lens.set_near_far(1, 60)
        sun_np = self.render.attach_new_node(sun)
        sun_np.set_pos(-12, -16, 24)
        sun_np.look_at(0, 0, 0)
        self.render.set_light(sun_np)

        sky = AmbientLight("sky")
        sky.set_color((0.35, 0.40, 0.50, 1))
        self.render.set_light(self.render.attach_new_node(sky))

    def save_screenshot(self, path: Path) -> None:
        self.screenshot(Filename.from_os_specific(str(path)), defaultFilename=False)


def run(screenshot: Path | None = None) -> None:
    """Open the game. With `screenshot`, render a few frames offscreen, save one and quit."""
    app = GameApp(offscreen=screenshot is not None)
    if screenshot is None:
        app.run()
        return
    for _ in range(5):
        app.taskMgr.step()
    app.save_screenshot(screenshot)
    app.destroy()

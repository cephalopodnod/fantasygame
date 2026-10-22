"""BG3-style camera: WASD/arrows pan, Q/E or middle-mouse drag rotate, mouse wheel zooms.

The camera orbits a focus point on the ground. A pivot node sits on the focus point and is
turned by yaw (heading) and pitch; the camera hangs `distance` metres behind it.
"""

import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import (
    AsyncTask,
    ButtonHandle,
    ClockObject,
    KeyboardButton,
    MouseButton,
    NodePath,
    Point3,
)

PAN_SPEED = 1.0
"""Ground covered per second, as a fraction of the camera distance."""
ROTATE_SPEED = 90.0
"""Degrees per second for Q/E."""
DRAG_ROTATE_SPEED = 180.0
"""Degrees per full window width/height of middle-mouse drag."""
ZOOM_STEP = 1.15
MIN_DISTANCE, MAX_DISTANCE = 4.0, 40.0
MIN_PITCH, MAX_PITCH = -85.0, -15.0


class CameraRig:
    def __init__(
        self,
        base: ShowBase,
        focus: Point3,
        yaw: float = 0.0,
        pitch: float = -50.0,
        distance: float = 16.0,
    ) -> None:
        self._base = base
        self.focus = Point3(focus)
        self.yaw = yaw
        self.pitch = pitch
        self.distance = distance
        self._last_mouse: tuple[float, float] | None = None

        assert base.camera is not None, "CameraRig needs a window with a camera"
        self._camera: NodePath = base.camera
        base.disableMouse()  # turn off Panda3D's default trackball camera
        self._pivot: NodePath = base.render.attach_new_node("camera-pivot")
        self._camera.reparent_to(self._pivot)

        base.accept("wheel_up", self.zoom, [1 / ZOOM_STEP])
        base.accept("wheel_down", self.zoom, [ZOOM_STEP])
        base.taskMgr.add(self._update, "camera-rig")
        self._apply()

    def zoom(self, factor: float) -> None:
        self.distance = min(MAX_DISTANCE, max(MIN_DISTANCE, self.distance * factor))
        self._apply()

    def _update(self, task: AsyncTask) -> int:
        dt = ClockObject.get_global_clock().get_dt()
        watcher = self._base.mouseWatcherNode
        if watcher is None:  # no window to take input from (offscreen rendering)
            return AsyncTask.DS_cont

        def held(*buttons: ButtonHandle) -> bool:
            return any(watcher.is_button_down(b) for b in buttons)

        key = KeyboardButton.ascii_key

        # Pan relative to where the camera is facing.
        forward = int(held(key("w"), KeyboardButton.up())) - int(
            held(key("s"), KeyboardButton.down())
        )
        right = int(held(key("d"), KeyboardButton.right())) - int(
            held(key("a"), KeyboardButton.left())
        )
        if forward or right:
            step = PAN_SPEED * self.distance * dt
            h = math.radians(self.yaw)
            self.focus.x += (-math.sin(h) * forward + math.cos(h) * right) * step
            self.focus.y += (math.cos(h) * forward + math.sin(h) * right) * step

        self.yaw += (int(held(key("q"))) - int(held(key("e")))) * ROTATE_SPEED * dt

        # Middle-mouse drag: left/right turns, up/down tilts.
        if watcher.has_mouse() and watcher.is_button_down(MouseButton.two()):
            mouse = (watcher.get_mouse_x(), watcher.get_mouse_y())
            if self._last_mouse is not None:
                self.yaw -= (mouse[0] - self._last_mouse[0]) / 2 * DRAG_ROTATE_SPEED
                self.pitch += (mouse[1] - self._last_mouse[1]) / 2 * DRAG_ROTATE_SPEED
            self._last_mouse = mouse
        else:
            self._last_mouse = None

        self._apply()
        return AsyncTask.DS_cont

    def _apply(self) -> None:
        self.pitch = min(MAX_PITCH, max(MIN_PITCH, self.pitch))
        self._pivot.set_pos(self.focus)
        self._pivot.set_hpr(self.yaw, self.pitch, 0)
        self._camera.set_pos(0, -self.distance, 0)
        self._camera.set_hpr(0, 0, 0)

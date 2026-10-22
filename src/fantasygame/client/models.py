"""Loading models by their asset-manifest entry."""

import gltf
from direct.actor.Actor import Actor
from panda3d.core import Filename, NodePath

from fantasygame.content.manifest import ModelEntry


def load_actor(entry: ModelEntry) -> Actor:
    """An animated model, scaled to metres, facing +Y, with its hidden parts removed.

    Parent it under its own node and move/turn that node, so the manifest's fix-ups stay put.
    """
    # Calls panda3d-gltf directly: Panda3D finds that loader through package metadata,
    # which a packaged .exe doesn't have.
    model = NodePath(gltf.load_model(Filename.from_os_specific(str(entry.path))))
    actor = Actor(model)
    actor.set_scale(entry.scale)
    actor.set_h(entry.heading)
    for part in entry.hidden_parts:
        found = actor.find(f"**/{part}")
        if found.is_empty():
            raise ValueError(f"Model {entry.id!r} has no part named {part!r}")
        found.remove_node()
    return actor

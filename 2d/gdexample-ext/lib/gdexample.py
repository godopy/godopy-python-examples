import numpy as np

from godot.core import GDCLASS
from godot.classdb import Sprite2D
from godot.types import Vector2


@GDCLASS(Sprite2D)
class GDExample:
    __slots__ = ['time_passed']

    def __init__(self):
        self.time_passed = 0.0

    def _process(self, delta: float) -> None:
        self.time_passed += delta

        new_position = Vector2(
            10.0 + (10.0 * np.sin(self.time_passed * 2.0)),
            10.0 + (10.0 * np.cos(self.time_passed * 1.5))
        )

        self.set_position(new_position)

import numpy as np

from godot import PropertyHint
from godot.core import GDCLASS
from godot.types import Vector2
from godot.classdb import Sprite2D, ClassDB
from godot.property_info import PropertyInfo


@GDCLASS(Sprite2D)
class GDExample:
    __slots__ = ['time_passed', 'amplitude', 'speed']

    @classmethod
    def _bind_methods(cls):
        ClassDB.bind_method(cls.set_amplitude)
        ClassDB.bind_method(cls.get_amplitude)
        cls.add_property(PropertyInfo(float, 'amplitude'), 'set_amplitude', 'get_amplitude')

        ClassDB.bind_method(cls.set_speed)
        ClassDB.bind_method(cls.get_speed)
        speed = PropertyInfo(float, 'speed', PropertyHint.PROPERTY_HINT_RANGE, '0,20,0.01')
        cls.add_property(speed, 'set_speed', 'get_speed')

    def __init__(self):
        self.time_passed = 0.0
        self.amplitude = 10.0
        self.speed = 1.0

    def set_amplitude(self, value: float) -> None:
        self.amplitude = value

    def get_amplitude(self) -> float:
        return self.amplitude

    def set_speed(self, value: float) -> None:
        self.speed = value

    def get_speed(self) -> float:
        return self.speed

    def _process(self, delta: float) -> None:
        self.time_passed += self.speed * delta

        time_passed = self.time_passed
        amplitude = self.amplitude

        new_position = Vector2(
            amplitude + (amplitude * np.sin(time_passed * 2.0)),
            amplitude + (amplitude * np.cos(time_passed * 1.5))
        )

        self.set_position(new_position)

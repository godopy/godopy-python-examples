import numpy as np

from godot.core import GDCLASS
from godot.enums import PropertyHint
from godot.types import Vector2
from godot.classdb import Sprite2D
from godot.property_info import PropertyInfo, PropertyInfoRange


@GDCLASS(Sprite2D)
class GDExample:
    __slots__ = ['time_passed', 'time_emit', 'amplitude', 'speed']

    @classmethod
    def _bind_methods(cls):
        cls.bind_method(cls.set_amplitude)
        cls.bind_method(cls.get_amplitude)
        cls.add_property(PropertyInfo(float, 'amplitude'), 'set_amplitude', 'get_amplitude')

        cls.bind_method(cls.set_speed)
        cls.bind_method(cls.get_speed)
        cls.add_property(PropertyInfoRange('speed', slice(0, 20, 0.01)), 'set_speed', 'get_speed')

        cls.add_signal('position_changed', PropertyInfo(Sprite2D, 'node'), PropertyInfo(Vector2, 'new_pos'))


    def __init__(self):
        self.time_passed = 0.0
        self.time_emit = 0.0
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

        self.time_emit += delta
        if self.time_emit > 1.0:
            self.emit_signal('position_changed', self, new_position)
            self.time_emit = 0.0

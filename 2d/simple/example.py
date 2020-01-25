import os
import math
import numpy as np

from godot import bindings
from godot.core.signals import SignalArgumentObject as SAO, SignalArgumentVector2 as SAV2
from godot.nativescript import register_method, register_property, register_signal, register_class

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class Logo(bindings.Sprite):
    def _init(self):
        with open(os.path.join(DATA_DIR, 'godopy-logo.png'), 'rb') as fp:
            ar = np.frombuffer(fp.read(), dtype=np.uint8)

        image = bindings.Image()
        image.load_png_from_buffer(ar)

        self.texture = bindings.ImageTexture()
        self.texture.create_from_image(image)

        self.centered = False
        self.time_emit = 0
        self.time_passed = 0.0
        self.amplitude = 10
        self._position = np.array([0, 0], dtype=np.float32)

    def _process(self, delta):
        self.time_passed += delta

        self._position[0] = self.amplitude + (self.amplitude * math.sin(self.time_passed * 2.0))
        self._position[1] = self.amplitude + (self.amplitude * math.cos(self.time_passed * 1.5))

        self.position = self._position  # Vector2 instance would also work

        self.time_emit += delta

        if self.time_emit >= 2:
            self.emit_signal('position_changed', self, self.position)
            self.time_emit = 0

    def __repr__(self):
        return '<Logo(%s) instance at 0x%x>' % (self.__class__.__bases__[0].__name__, hash(self))

    @staticmethod
    def _register_methods():
        register_method(Logo, '_process')
        register_property(Logo, 'amplitude', 10)

        register_signal(Logo, 'position_changed', SAO('node'), SAV2('new_position'))


class Example(bindings.Node2D):
    def _init(self):
        self.logo = Logo()
        self.add_child(self.logo)

    def _ready(self):
        self.logo.connect('position_changed', self, '_on_position_changed')

    def _on_position_changed(self, node, new_position):
        print(node, new_position)

    @staticmethod
    def _register_methods():
        register_method(Example, '_ready')
        register_method(Example, '_on_position_changed')


class Main(bindings.SceneTree):
    def _init(self):
        self.example = Example()
        self.get_root().add_child(self.example)

    @staticmethod
    def _register_methods():
        pass


def _init():
    register_class(Logo)
    register_class(Example)
    register_class(Main)

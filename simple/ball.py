'''
Simple things should be simple

Ported from https://www.pygame.org/docs/tut/PygameIntro.html
'''

import os
import numpy as np

from godot import bindings
from godot.core.types import Vector2
from godot.globals import gdclass
from godot.nativescript import register_class

with open(os.path.join(os.path.dirname(__file__), 'data', 'intro-ball.png'), 'rb') as fp:
    IMAGE_DATA = np.frombuffer(fp.read(), dtype=np.uint8)

SIZE = Vector2(320, 240)  # XXX: Size2 doesn't work yet

speed = Vector2(2, 2).to_numpy()

x_max = SIZE.x
y_max = SIZE.y


@gdclass(bindings.Sprite, '_process')
def Ball(self, delta):
    self.position += speed

    if self.position.x < 0 or self.position.x > x_max:
        speed[0] = -speed[0]
    if self.position.y < 0 or self.position.y > y_max:
        speed[1] = -speed[1]


@gdclass(bindings.SceneTree, '_init')
def Main(self):
    global x_max, y_max

    scene = bindings.Node2D()

    image = bindings.Image()
    image.load_png_from_buffer(IMAGE_DATA)
    x_max -= image.get_width()
    y_max -= image.get_height()

    ball = Ball()

    ball.texture = bindings.ImageTexture()
    ball.texture.create_from_image(image)
    ball.centered = False

    scene.add_child(ball)
    self.get_root().add_child(scene)


def _init():
    bindings.OS.set_window_size(SIZE)
    register_class(Ball)
    register_class(Main)

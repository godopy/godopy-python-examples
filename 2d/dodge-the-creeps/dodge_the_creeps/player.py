import numpy as np

from godot import bindings
from godot.bindings import Input
from godot.core.types import Vector2

from godot.nativescript import register_class, register_method, register_property, register_signal

INPUT_MAP = {
    'ui_right': Vector2(1, 0).to_numpy(),
    'ui_left': Vector2(-1, 0).to_numpy(),
    'ui_up': Vector2(0, -1).to_numpy(),
    'ui_down': Vector2(0, 1).to_numpy()
}.items()


class Player(bindings.Area2D):
    def _init(self):
        self.speed = 400
        self.screen_size = None

    def _ready(self):
        self.screen_size = self.get_viewport_rect().size.to_numpy()
        print('SCREEN SIZE:', self.screen_size)
        self.hide()

    @property
    def sprite(self):
        return self.find_node('AnimatedSprite')

    @property
    def shape(self):
        return self.find_node('CollisionShape2D')

    def _process(self, delta):
        velocity = Vector2().to_numpy()

        for event_key, vec in INPUT_MAP:
            if Input.is_action_pressed(event_key):
                velocity += vec

        if velocity.any():
            velocity = velocity/np.linalg.norm(velocity) * self.speed
            self.sprite.play()
        else:
            self.sprite.stop()

        pos = self.position.to_numpy() + velocity * delta
        self.position = Vector2.from_numpy(np.clip(pos, 0, self.screen_size))

        if velocity[0]:
            self.sprite.animation = 'right'
            self.sprite.flip_v = False
            self.sprite.flip_h = velocity[0] < 0
        elif velocity[1]:
            self.sprite.animation = 'up'
            self.sprite.flip_v = velocity[1] > 0

    def _on_Player_body_entered(self, body):
        # TODO: GodoPy should pass a correct wrapper for the "body" argument (not None as it is now)
        self.hide()
        self.emit_signal('hit')
        self.shape.set_deferred('disabled', True)

    def start(self, pos):
        self.position = pos
        self.show()
        self.shape.disabled = False

    @staticmethod
    def _register_methods():
        register_method(Player, '_ready')
        register_method(Player, '_process')
        register_method(Player, '_on_Player_body_entered')
        register_method(Player, 'start')

        register_property(Player, 'speed', 400)
        register_signal(Player, 'hit')


def _init():
    register_class(Player)

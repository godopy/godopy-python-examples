from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parents[1]

GODOT_PROJECT = BASE_DIR / '__godot__'

PYTHON_PACKAGE = 'dodge_the_creeps'
GDNATIVE_LIBRARY = 'dodge-the-creeps.gdnlib'

NAME = 'Dodge the Creeps'
MAIN_SCENE = 'res://Main.tscn'
ICON = 'res://icon.png'

WINDOW_SIZE = (480, 720)


DEVELOPMENT_PATH = BASE_DIR

NATIVESCRIPT_EXTENSIONS = [
    'scripts/TermShell',
    'Player'
]

INPUT = {
    'move_left': {
        'dead_zone': 0.5,
        'events': []  # TODO
    },
    # TODO
}

DEFAULT_ENVIRONMENT = 'res://default_env.tres'

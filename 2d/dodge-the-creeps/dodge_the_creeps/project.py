from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parents[1]

GODOT_PROJECT = BASE_DIR / 'gd' / 'dodge_the_creeps'

PYTHON_PACKAGE = 'dodge_the_creeps'
GDNATIVE_LIBRARY = 'dodge-the-creeps.gdnlib'

DEVELOPMENT_PATH = BASE_DIR

NATIVESCRIPT_EXTENSIONS = [
    'scripts/TermShell',
    'Player'
]

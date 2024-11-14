import sys

import godot
from godot.core import GDREGISTER_CLASS
from gdexample import GDExample


def initialize(level):
    if level != godot.MODULE_INITIALIZATION_LEVEL_SCENE:
        return

    GDREGISTER_CLASS(GDExample)

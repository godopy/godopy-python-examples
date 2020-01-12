from . import player

try:
    from .scripts import term_shell
    TOOLS = True
except ModuleNotFoundError:
    TOOLS = False


def _nativescript_init():
    if TOOLS:
        term_shell._init()

    player._init()

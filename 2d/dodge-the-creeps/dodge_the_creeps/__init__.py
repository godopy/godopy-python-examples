from godot.nativescript import register_class, register_tool_class

from . import player

try:
    from .scripts import term_shell
    TOOLS = True
except ModuleNotFoundError:
    TOOLS = False


def _nativescript_init():
    if TOOLS:
        register_tool_class(term_shell.TermShell)

    register_class(player.Player)

from godot import bindings
from godot.globals import gdclass
from godot.nativescript import register_tool_class, gdmethod

from IPython.terminal.embed import InteractiveShellEmbed

POLL_INTERVAL = 0.05


class GodotPythonShell(InteractiveShellEmbed):
    def init_virtualenv(self):
        pass

    def interact(self):
        print(self.separate_in, end='')

        try:
            code = self.prompt_for_code()
        except EOFError:
            if self.ask_yes_no('Do you really want to exit ([y]/n)?', 'y', 'n'):
                self.ask_exit()
        else:
            if code:
                self.run_cell(code, store_history=True)

        return not self.keep_running


@gdclass
class Main(bindings.MainLoop):
    @gdmethod
    def _initialize(self):
        self.ipshell = GodotPythonShell()
        self.ipshell.show_banner()
        self.ipshell.keep_running = True

        self.time_elapsed = 0

    @gdmethod
    def _idle(self, delta):
        self.time_elapsed += delta

        if self.time_elapsed >= POLL_INTERVAL:
            self.time_elapsed = 0
            return self.ipshell.interact()


def _init():
    register_tool_class(Main)

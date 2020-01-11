"""
TODO: Move to `godopy/contrib/scripts/` and allow installation from there
"""
from godot import bindings
from godot.nativescript import register_method

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


class TermShell(bindings.MainLoop):
    def _initialize(self):
        self.ipshell = GodotPythonShell()
        self.ipshell.show_banner()
        self.ipshell.keep_running = True

        self.time_elapsed = 0

    def _idle(self, delta):
        self.time_elapsed += delta

        if self.time_elapsed >= POLL_INTERVAL:
            self.time_elapsed = 0
            return self.ipshell.interact()

    @staticmethod
    def _register_methods():
        register_method(TermShell, '_initialize', TermShell._initialize)
        register_method(TermShell, '_idle', TermShell._idle)

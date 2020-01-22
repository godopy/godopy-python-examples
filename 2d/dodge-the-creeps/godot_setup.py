from godot_tools.setup import godot_setup
from godot_tools.setup.libraries import GenericGDNativeLibrary
from godot_tools.setup.extensions import NativeScript


godot_setup(
    godot_project='gd/dodge_the_creeps',
    package='dodge_the_creeps',
    # set_development_path=True,
    library=GenericGDNativeLibrary('dodge-the-creeps.gdnlib', singleton=False),
    extensions=[
        NativeScript('scripts/TermShell.gdns', class_name='TermShell'),

        NativeScript('Player.gdns', class_name='Player')
    ]
)

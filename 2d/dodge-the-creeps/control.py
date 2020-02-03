#!/usr/bin/env python
"""GodoPy's command-line utility for administrative tasks."""
import os


def main():
    """Run administrative tasks."""
    os.environ.setdefault('GODOPY_PROJECT_MODULE', 'dodge_the_creeps.project')
    try:
        from godot_tools.cli import godopy
    except ImportError as exc:
        raise ImportError(
            "Couldn't import GodoPy. Are you sure it's installed? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    godopy()


if __name__ == '__main__':
    main()

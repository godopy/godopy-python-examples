# Python examples for GodoPy

Godot executable must be on PATH

```
$ # Activate virtualenv
$ pip install GodoPy
```

## 2D

### Dodge the Creeps

```
$ cd 2d/dodge-the-creeps
$ ./control.py installscripts  # Doesn't work under 0.0.1
$ ./control.py runeditor  # Reimport assets
$ ./control.py run
$ ./control.py runscript res://scripts/TermShell.gdns  # Executes scripts/term_shell.py
```

## Simple

```
$ cd simple
$ godopy enable-runpy
$ godopy runpy example
$ godopy runpy ball
$ godopy runpy term_shell
```

import tkinter as tk

def Button(
    screen_obj = None,
    **kwargs
) -> None:
    if screen_obj is None:
        raise TypeError("Parameter \"screen_obj\" must be specified.")
    return tk.Button(screen_obj.root, **kwargs).pack(**kwargs)

import tkinter as tk
from typing import Optional

def Button(
    screen_obj = None,
    packargs: Optional[dict] = None,
    **kwargs
) -> None:
    if packargs is None:
        packargs = {}
    if screen_obj is None:
        raise TypeError("Parameter \"screen_obj\" must be specified.")
    return tk.Button(screen_obj.root, **kwargs).pack(**packargs)

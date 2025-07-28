import tkinter as tk
from typing import Optional

class Button:
    def __init__(
        self,
        screen_obj=None,
        packargs: Optional[dict] = None,
        **kwargs
    ) -> None:
        if screen_obj is None:
            raise TypeError('Parameter "screen_obj" must be specified.')

        if packargs is None:
            packargs = {}

        tk.Button(screen_obj.root, **kwargs).pack(**packargs)

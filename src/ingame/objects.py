import tkinter as tk
from typing import Optional, Any
from .core import Screen

class Button:
    button_obj: tk.Button

    def __init__(
        self,
        screen_obj: Optional[Screen] = None,
        /,
        packargs: Optional[dict[Any, Optional[Any]]] = None,
        **kwargs: Any
    ) -> None:
        if screen_obj is None:
            raise TypeError('Parameter "screen_obj" must be specified.')

        if packargs is None:
            packargs = {}

        self.button_obj = tk.Button(screen_obj.root, **kwargs)
        self.button_obj.pack(**{k: v for k, v in packargs.items() if v is not None})
    def destroy(
        self
    ) -> None:
        """Destroy button"""

        self.button_obj.destroy()

class Text:
    text_obj: tk.Label

    def __init__(
        self,
        screen_obj: Optional[Screen] = None,
        /,
        packargs: Optional[dict[Any, Optional[Any]]] = None,
        **kwargs: Any
    ) -> None:
        if screen_obj is None:
            raise TypeError('Parameter "screen_obj" must be specified.')

        if packargs is None:
            packargs = {}

        self.text_obj = tk.Label(screen_obj.root, **kwargs)
        self.text_obj.pack(**{k: v for k, v in packargs.items() if v is not None})
    def destroy(
        self
    ) -> None:
        """Destroy text"""

        self.text_obj.destroy()

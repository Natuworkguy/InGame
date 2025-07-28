import tkinter as tk
from typing import Optional, Any

class Button:
    def __init__(
        self,
        screen_obj: Optional[Any] = None,
        /,
        packargs: Optional[dict[Any, Optional[Any]]] = None,
        **kwargs: Any
    ) -> None:
        if screen_obj is None:
            raise TypeError('Parameter "screen_obj" must be specified.')

        if packargs is None:
            packargs = {}

        tk.Button(screen_obj.root, **kwargs).pack(**{k: v for k, v in packargs.items() if v is not None})

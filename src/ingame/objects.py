import tkinter as tk
from typing import Optional, Any
from abc import ABC, abstractmethod
from .core import Screen

class Object(ABC):
    """
    Base object class
    """

    def __init__(
        self
    ) -> None: ...

    @abstractmethod
    def config(
        self
    ) -> None: ...

    @abstractmethod
    def destroy(
        self
    ) -> None: ...

class Button(Object):
    """
    Creates a Button on the given Screen, packs it with optional args,
    and provides a destroy() method for cleanup.
    """

    button_obj: tk.Button

    def __init__(
        self,
        screen_obj: Screen,
        /,
        packargs: Optional[dict[Any, Optional[Any]]] = None,
        **kwargs: Any
    ) -> None:
        if not isinstance(screen_obj, Screen):
            raise TypeError("screen_obj must be an instance of Screen")

        if packargs is None:
            packargs = {}

        self.button_obj = tk.Button(screen_obj.root, **kwargs)
        self.button_obj.pack(**{k: v for k, v in packargs.items() if v is not None})

    def config(
        self,
        **kwargs
    ) -> None:
        """Configure object"""

        self.button_obj.config(**kwargs)

    def destroy(
        self
    ) -> None:
        """Destroy button"""

        self.button_obj.destroy()

class Text(Object):
    """
    Creates text on the given Screen, packs it with optional args,
    and provides a destroy() method for cleanup.
    """

    text_obj: tk.Label

    def __init__(
        self,
        screen_obj: Screen,
        /,
        packargs: Optional[dict[Any, Optional[Any]]] = None,
        **kwargs: Any
    ) -> None:
        if not isinstance(screen_obj, Screen):
            raise TypeError("screen_obj must be an instance of Screen")

        if packargs is None:
            packargs = {}

        self.text_obj = tk.Label(screen_obj.root, **kwargs)
        self.text_obj.pack(**{k: v for k, v in packargs.items() if v is not None})

    def config(
        self,
        **kwargs
    ) -> None:
        """Configure object"""

        self.text_obj.config(**kwargs)


    def destroy(
        self
    ) -> None:
        """Destroy text"""

        self.text_obj.destroy()

class Image(Object):
    """
    Displays an image (from file or URL) on the given Screen, packs it with optional args,
    and provides a destroy() method for cleanup. Supports basic transformations (resize, scale, position).
    """

    image_obj: tk.Label
    _photo_image: Any

class Input(Object):
    """
    Creates a single line text input box on the given Screen, packs it with optional args,
    and provides a destroy() method for cleanup.
    """

    input_obj: tk.Entry

    def __init__(
        self,
        screen_obj: Screen,
        /,
        packargs: Optional[dict[Any, Optional[Any]]] = None,
        **kwargs: Any
    ) -> None:
        if not isinstance(screen_obj, Screen):
            raise TypeError("screen_obj must be an instance of Screen")

        if packargs is None:
            packargs = {}

        self.input_obj = tk.Entry(screen_obj.root, **kwargs)
        self.input_obj.pack(**{k: v for k, v in packargs.items() if v is not None})

    def get(
        self
    ) -> str:
        """Get input box value"""

        return self.input_obj.get()

    def config(
        self,
        **kwargs
    ) -> None:
        """Configure object"""

        self.input_obj.config(**kwargs)

    def destroy(
        self
    ) -> None:
        """Destroy text"""

        self.input_obj.destroy()

# How to Make Your Own Objects in InGame

This guide explains how to create custom objects (UI components) for use with the [InGame](https://github.com/Natuworkguy/InGame) library, following the exact conventions and code style used by the InGame developers in [`src/ingame/objects.py`](https://github.com/Natuworkguy/InGame/blob/main/src/ingame/objects.py).

---

## 1. Inherit from the `Object` Base Class

All custom objects must inherit from the `Object` abstract base class:

```python
from abc import ABC, abstractmethod

class Object(ABC):
    def __init__(self) -> None:
        ...

    @abstractmethod
    def config(self) -> None:
        ...

    @abstractmethod
    def destroy(self) -> None:
        ...
```

This ensures all objects provide `config()` and `destroy()` methods.

---

## 2. Implement the Required Methods

A custom object should:

- Accept a `Screen` instance as the first argument (`screen_obj`)
- Optionally accept a `packargs` dictionary for packing options
- Accept further widget-specific keyword arguments (`**kwargs`)
- Create a tkinter widget (e.g., `tk.Button`, `tk.Label`, etc.) as an attribute
- Use `pack()` for geometry management, filtering out `None` values from `packargs`
- Implement `config()` and `destroy()` methods

### Example: Custom Widget Template

```python
import tkinter as tk
from ingame.core import Screen
from ingame.objects import Object

class CustomWidget(Object):
    def __init__(
        self,
        screen_obj: Screen,
        /,
        packargs: dict = None,
        **kwargs
    ) -> None:
        if not isinstance(screen_obj, Screen):
            raise TypeError("screen_obj must be an instance of Screen")
        
        if packargs is None:
            packargs = {}
        
        self.widget_obj = tk.Label(screen_obj.root, **kwargs)  # Replace with desired widget type
        self.widget_obj.pack(**{k: v for k, v in packargs.items() if v is not None})

    def config(self, **kwargs) -> None:
        self.widget_obj.config(**kwargs)

    def destroy(self) -> None:
        self.widget_obj.destroy()
```

---

## 3. Example from InGame: Button

```python
class Button(Object):
    def __init__(
        self,
        screen_obj: Screen,
        /,
        packargs: dict = None,
        **kwargs
    ) -> None:
        if not isinstance(screen_obj, Screen):
            raise TypeError("screen_obj must be an instance of Screen")
        if packargs is None:
            packargs = {}
        self.button_obj = tk.Button(screen_obj.root, **kwargs)
        self.button_obj.pack(**{k: v for k, v in packargs.items() if v is not None})

    def config(self, **kwargs) -> None:
        self.button_obj.config(**kwargs)

    def destroy(self) -> None:
        self.button_obj.destroy()
```

---

## 4. Usage Example

```python
from ingame.core import InGame, Screen
from ingame.objects import CustomWidget

app = InGame()
screen = Screen(app)

my_widget = CustomWidget(screen, text="Hello, InGame!", packargs={"pady": 10})
my_widget.config(bg="blue")
# ...
```

---

## 5. Notes

- Always check that `screen_obj` is an instance of `Screen`.
- Use `packargs` to pass layout options (e.g., `{"pady": 10}`).
- Expose widget-specific methods as needed (e.g., `get()` for text input).
- Follow the pattern in [`src/ingame/objects.py`](https://github.com/Natuworkguy/InGame/blob/main/src/ingame/objects.py) for consistency.

If you find this line of code, congradulations! You owe Kath $35 dollars now. It's not a choice. Pay up.

from functools import wraps
from typing import Callable, Any, Optional
import inspect
from enum import Enum
import tkinter as tk

class InGameException(Exception):
    """Exception for InGame module"""
    pass

class EventType:
    class Key(Enum):
        A = "A"
        B = "B"
        C = "C"
        D = "D"
        E = "E"
        F = "F"
        G = "G"
        H = "H"
        I = "I"
        J = "J"
        K = "K"
        L = "L"
        M = "M"
        N = "N"
        O = "O"
        P = "P"
        Q = "Q"
        R = "R"
        S = "S"
        T = "T"
        U = "U"
        V = "V"
        W = "W"
        X = "X"
        Y = "Y"
        Z = "Z"
        UP = "UP"
        DOWN = "DOWN"
        LEFT = "LEFT"
        RIGHT = "RIGHT"
        BACKSPACE = "BACKSPACE"
        ENTER = "RETURN"
        ESCAPE = "ESCAPE"

EventsType = EventType.Key

class InGame:
    events: dict[EventsType, Callable[[], None]]

    def __init__(self) -> None:
        self.events = {}

    def event(
        self,
        /,
        type: Optional[EventsType] = None
    ) -> Callable[[Callable[[], Any]], Callable[[], None]]:
        if type is None:
            raise InGameException("Parameter 'type' must be specified.")

        def decorator(func: Callable[[], Any]) -> Callable[[], None]:
            if not inspect.isfunction(func):
                raise InGameException("Parameter 'func' must be a function.")

            @wraps(func)
            def wrapper() -> None:
                self.events[type] = func

            wrapper()
            return wrapper

        return decorator

    def trigger_event(
        self,
        type: EventsType
    ) -> None:
        func = self.events.get(type)
        if func is None:
            raise InGameException(f"No event for {type.name}")
        func()

class Screen:
    def __init__(
        self,
        ingame_obj: InGame,
        *,
        width: int = 400,
        height: int = 300,
        title: str = "InGame Window"
    ) -> None:
        def on_key_press(event: tk.Event) -> None:
            key = event.keysym.upper()
            if key in EventType.Key.__members__:
                try:
                    ingame_obj.trigger_event(EventType.Key[key])
                except InGameException:
                    pass

        self.root = tk.Tk()
        self.root.title(title)
        self.root.bind("<KeyPress>", on_key_press)
        self.root.geometry(f"{width}x{height}")

    def set_icon(self, path: str, **kwargs) -> None:
        self.root.iconbitmap(path, **kwargs)

    def show(self) -> None:
        self.root.mainloop()

    def quit(self) -> None:
        self.root.destroy()

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
    """InGame main application"""
    events: dict[EventsType, Callable[[], None]]

    def __init__(self) -> None:
        self.events = {}

    def event(
        self,
        /,
        type: Optional[EventsType] = None
    ) -> Callable[[Callable[[], Optional[Any]]], Callable[[], None]]:
        """
        Decorator to Register an event to the InGame application
        Parameters:
            type: Optional[EventsType]
        """
        if type is None:
            raise InGameException("Parameter 'type' must be specified.")

        def decorator(func: Callable[[], Optional[Any]]) -> Callable[[], None]:
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
        """
        Triggers a registered event in the InGame application.
        Parameters:
            type: EventsType
        """
        if not isinstance(type, EventsType):
            raise InGameException(f"Type argument must be of type EventsType, not {type.__class__.__name__}")
        func: Optional[Callable[[], Any]] = self.events.get(type)
        if func is None:
            raise InGameException(f"No event for {type.name}")
        func()

    def clear_events(
        self
    ) -> None:
        """Clears all registered events"""
        self.events = {}

class Screen:
    """Application window"""
    root: tk.Tk
    def __init__(
        self,
        ingame_obj: InGame,
        *,
        width: int = 400,
        height: int = 300,
        title: str = "InGame Window"
    ) -> None:
        def on_key_press(event: tk.Event) -> None:
            key: str = event.keysym.upper()
            if key in EventType.Key.__members__:
                try:
                    ingame_obj.trigger_event(EventType.Key[key])
                except InGameException:
                    pass

        self.root = tk.Tk()
        self.root.title(title)
        self.root.bind("<KeyPress>", on_key_press)
        self.root.geometry(f"{width}x{height}")

    def show(
        self
    ) -> None:
        """Show the window"""
        self.root.mainloop()

    def quit(
        self
    ) -> None:
        """Quit the window"""
        self.root.destroy()

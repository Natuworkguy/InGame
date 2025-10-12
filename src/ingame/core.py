from functools import wraps
from typing import Callable, Any, Optional, Union, NoReturn
import inspect
from enum import Enum
import tkinter as tk

class InGameException(Exception):
    """Exception for InGame module"""

    pass

class EventType:
    """Events that are detectable using the `@InGame.event` decorator"""

    class Key(Enum):
        """Detect key press"""

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
        CAPS_LOCK = "CAPS_LOCK"
        CONTROL_L = "CONTROL_L"
        CONTROL_R = "CONTROL_R"

        F1 = "F1"
        F2 = "F2"
        F3 = "F3"
        F4 = "F4"
        F5 = "F5"
        F6 = "F6"
        F7 = "F7"
        F8 = "F8"
        F9 = "F9"
        F10 = "F10"

        EQUAL = "EQUAL"
        SLASH = "SLASH"
        BACKSLASH = "BACKSLASH"

        SHIFT_L = "SHIFT_L"
        SHIFT_R = "SHIFT_R"

EventsType = EventType.Key

class InGame:
    """InGame main application"""

    events: dict[EventsType, Callable[[], None]]

    def __init__(
        self
    ) -> None:
        self.events = {}

    def event(
        self,
        /,
        type: EventsType
    ) -> Union[Callable[[Callable[[], Optional[Any]]], Callable[[], None]], NoReturn]:
        """
        Decorator to Register an event to the InGame application

        Parameters:
            - type - `Optional[EventsType]`
        """

        if not isinstance(type, EventsType):
            raise InGameException("Parameter 'type' must be of type EventsType")

        def decorator(func: Callable[[], Optional[Any]]) -> Callable[[], None]:
            if not inspect.isfunction(func):
                raise InGameException("Parameter 'func' must be a function.")

            @wraps(wrapped=func)
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

    def clear_all_events(
        self
    ) -> None:
        """Clears all registered events"""

        self.events = {}

    def clear_event(
        self,
        event: EventsType
    ) -> None:
        self.events.pop(event, None)


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

        if not isinstance(width, int):
            raise InGameException(f"Width must be of type int, not {width.__class__.__name__}.")
        elif not isinstance(height, int):
            raise InGameException(f"Height must be of type int, not {height.__class__.__name__}.")

        self.root = tk.Tk()
        self.root.title(title)
        self.root.bind("<KeyPress>", on_key_press)
        self.root.geometry(f"{str(width)}x{str(height)}")

    def set_resize(
        self,
        width: bool,
        height: bool
    ) -> None:
        """Set if window can be resized"""

        if not isinstance(width, bool):
            raise InGameException("'width' parameter must be of type bool.")
        elif not isinstance(height, bool):
            raise InGameException("'height' parameter must be of type bool.")

        self.root.resizable(width, height)

    def show(
        self
    ) -> None:
        """Show the window"""

        self.root.mainloop()

    def after(
        self,
        ms: int,
        func: Callable[..., None],
        *args: Any
    ) -> None:
        """Call a function after a certain amount of milliseconds"""

        if not isinstance(ms, int):
            raise InGameException(f"'ms' parameter must be of type int, not {ms.__class__.__name__}.")
        elif not inspect.isfunction(func) and not inspect.ismethod(func):
            raise InGameException("'func' parameter must be a function or method.")

        self.root.after(ms, func, *args)

    def quit(
        self
    ) -> None:
        """Quit the window"""

        self.root.destroy()

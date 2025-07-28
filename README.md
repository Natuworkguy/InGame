# InGame 🎮

**InGame** is a lightweight Python library designed to simplify making amazing UIs within a basic GUI window using `tkinter`. It enables developers to easily register and trigger events based on key presses with clean, decorator-based syntax.

---

## ✨ Features

- ✅ Decorator-based event binding
- ✅ Enum-based key recognition (A–Z, arrows, Enter, Escape, etc.)
- ✅ Clean and extensible architecture
- ✅ Simple GUI rendering using `tkinter`

---

## 🚀 Getting Started

### 🔧 Installation

Use `pip install ingame` to install the project.

---

## 🧠 Usage Example

```python
from ingame.core import InGame, Screen, EventType

app = InGame()

@app.event(type=EventType.Key.A)
def handle_a():
    print("Key A pressed!")

@app.event(type=EventType.Key.ESCAPE)
def handle_escape():
    print("Escape pressed!")
    screen.quit()

screen = Screen(app, title="My InGame App", width=600, height=400)
screen.show()
````

---

## 🎮 Supported Keys

Supported via `EventType.Key`, including:

* A–Z
* Arrow keys: `UP`, `DOWN`, `LEFT`, `RIGHT`
* `ENTER`, `ESCAPE`, `BACKSPACE`

---

## 📦 Components

### `InGame`

Handles registering and triggering events:

* `@event(type: EventType.Key)`: Registers a function for a specific key event.
* `trigger_event(type)`: Manually triggers an event.

### `Screen`

Simple `tkinter` window with key event binding:

* `show()`: Opens the window and starts listening for key presses.
* `quit()`: Closes the window.

---

## ⚠️ Exceptions

* `InGameException`: Raised for invalid usage such as missing event type or unregistered keys.

---

## 🛠️ Development Notes

Written in Python 3.10+
Uses `tkinter`, `Enum`, and `inspect`.

---

## 📄 License

[MIT License](LICENSE)

---

## ❤️ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 👤 Author

Made with ❤️ by [Natuworkguy](https://github.com/Natuworkguy/)

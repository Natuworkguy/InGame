# InGame 🎮

**InGame** is a lightweight Python library designed to simplify making amazing UIs within a basic GUI window using `tkinter`. It enables developers to easily register and trigger events based on key presses with clean, decorator-based syntax.

<div align="center">
  <a href="http://python.org/"><img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" /></a>
  <a href="https://pypi.org/project/ingame/"><img src="https://img.shields.io/pypi/v/ingame?color=brightgreen&label=version" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Natuworkguy/InGame" /></a>
  <a href><img src="https://img.shields.io/github/stars/Natuworkguy/InGame?style=social" /></a>  
</div>

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
from ingame.objects import Text, Button

app = InGame()

@app.event(type=EventType.Key.A)
def handle_a():
    print("Key A pressed!")

@app.event(type=EventType.Key.ESCAPE)
def handle_escape():
    print("Escape pressed!")
    screen.quit()

screen = Screen(app, title="My InGame App", width=600, height=400)

screen.set_resize(True, True)

hello_text = Text(screen, text="Hello!")
Button(screen, text="Click me", command=hello_text.destroy)

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

[**`MIT License`**](https://github.com/Natuworkguy/InGame/blob/main/LICENSE)

---

## ❤️ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 👤 Author

Made with ❤️ by [Natuworkguy](https://github.com/Natuworkguy/)

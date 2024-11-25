
# MouseClickTool

MouseClickTool is a simple desktop application that automates mouse clicking. It's perfect for tasks that require repetitive clicking, such as gaming or testing. The tool is built with PyQt5 for the user interface and uses `pyautogui` for mouse control.

## Features

- **Customizable Click Interval**: Set the delay between mouse clicks in milliseconds.
- **Mouse Button Selection**: Choose between left or right mouse button clicking.
- **Hotkey Support**: Start/stop the clicking process with the F1 hotkey.
- **User-Friendly Interface**: Simple and intuitive UI with clear labels and instructions.

## Installation

1. Clone the repository or download the source code.
   ```bash
   git clone https://github.com/yourusername/mouseclicktool.git
   cd mouseclicktool
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python mouse_click_tool.py
   ```

## Usage

1. Open the application.
2. Set the interval (in milliseconds) for mouse clicks.
3. Choose the mouse button (left or right).
4. Press the "Start" button or use the `F1` hotkey to begin clicking.
5. Press "Stop" or the `F1` hotkey again to stop.

## Requirements

- Python 3.6 or later
- PyQt5
- pyautogui
- keyboard

## Notes

- Ensure the application has proper permissions if running on operating systems with strict security controls.
- The tool uses a global hotkey (`F1`). Avoid conflicts with other applications that might use the same hotkey.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

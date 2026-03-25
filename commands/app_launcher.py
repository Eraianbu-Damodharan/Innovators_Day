import os
import webbrowser
from utils.window_focus import launch_and_focus, focus_existing_process


APP_MAP = {
    "notepad": {
        "processes": ["notepad.exe"],
        "command": "notepad.exe",
        "message": "Opening Notepad"
    },
    "calculator": {
        "processes": ["calculatorapp.exe", "calc.exe"],
        "command": "calc.exe",
        "message": "Opening Calculator"
    },
    "chrome": {
        "processes": ["chrome.exe"],
        "command": "start chrome",
        "message": "Opening Chrome"
    },
    "explorer": {
        "processes": ["explorer.exe"],
        "command": "explorer",
        "message": "Opening File Explorer"
    },
    "paint": {
        "processes": ["mspaint.exe"],
        "command": "mspaint.exe",
        "message": "Opening Paint"
    },
    "cmd": {
        "processes": ["cmd.exe"],
        "command": "start cmd",
        "message": "Opening Command Prompt"
    }
}


def open_desktop_app(app_key):
    app = APP_MAP.get(app_key)
    if not app:
        return f"Unknown app: {app_key}"

    if focus_existing_process(app["processes"]):
        return f"Bringing {app_key.title()} to front"

    return launch_and_focus(
        app["command"],
        app["message"],
        process_names=app["processes"]
    )


def open_web(url, message="Opening website"):
    try:
        webbrowser.open(url)
        return message
    except Exception as e:
        return f"Error: {e}"


def open_settings():
    try:
        os.system("start ms-settings:")
        return "Opening Settings"
    except Exception as e:
        return f"Error: {e}"
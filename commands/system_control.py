import os
import subprocess
from utils.security import resolve_alias_path, is_path_allowed, normalize_path

class SystemControl:
    def open_file_explorer(self) -> str:
        os.startfile(os.path.expanduser("~"))
        return "Opened File Explorer."

    def open_folder(self, path: str) -> str:
        resolved = resolve_alias_path(path)

        if not is_path_allowed(resolved):
            return "Access denied. Folder is outside allowed directories."

        folder = normalize_path(resolved)

        if not folder.exists() or not folder.is_dir():
            return "Folder not found."

        os.startfile(str(folder))
        return f"Opened folder: {folder}"

    def open_notepad(self) -> str:
        subprocess.Popen(["notepad.exe"])
        return "Opened Notepad."

    def open_calculator(self) -> str:
        subprocess.Popen(["calc.exe"])
        return "Opened Calculator."

    def open_chrome(self) -> str:
        possible_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]
        for path in possible_paths:
            if os.path.exists(path):
                subprocess.Popen([path])
                return "Opened Chrome."
        return "Chrome not found."
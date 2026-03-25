from pathlib import Path
from datetime import datetime, timedelta
from utils.security import resolve_alias_path, is_path_allowed, normalize_path

class CleanupManager:
    def create_file(self, path: str) -> str:
        if not is_path_allowed(path):
            return "Access denied. Path is outside allowed directories."

        p = normalize_path(path)
        p.parent.mkdir(parents=True, exist_ok=True)

        with open(p, "w", encoding="utf-8") as f:
            f.write("Jarvis created this file.")

        return f"File created: {p}"

    def delete_file(self, path: str) -> str:
        if not is_path_allowed(path):
            return "Access denied. Path is outside allowed directories."

        p = normalize_path(path)
        if p.exists() and p.is_file():
            send2trash(str(p))
            return f"File moved to Recycle Bin: {p}"
        return "File not found."

    def create_folder(self, path: str) -> str:
        if not is_path_allowed(path):
            return "Access denied. Path is outside allowed directories."

        p = normalize_path(path)
        p.mkdir(parents=True, exist_ok=True)
        return f"Folder created: {p}"

    def delete_folder(self, path: str) -> str:
        if not is_path_allowed(path):
            return "Access denied. Path is outside allowed directories."

        p = normalize_path(path)
        if p.exists() and p.is_dir():
            send2trash(str(p))
            return f"Folder moved to Recycle Bin: {p}"
        return "Folder not found."

    def rename_item(self, old_path: str, new_path: str) -> str:
        if not is_path_allowed(old_path) or not is_path_allowed(new_path):
            return "Access denied. Source or destination is outside allowed directories."

        old = normalize_path(old_path)
        new = normalize_path(new_path)

        if old.exists():
            old.rename(new)
            return f"Renamed to: {new}"
        return "Item not found."

    def move_item(self, source: str, destination: str) -> str:
        if not is_path_allowed(source) or not is_path_allowed(destination):
            return "Access denied. Source or destination is outside allowed directories."

        src = normalize_path(source)
        dst = normalize_path(destination)

        if src.exists():
            shutil.move(str(src), str(dst))
            return f"Moved {src} to {dst}"
        return "Source item not found."

    def list_files(self, path: str) -> str:
        if not is_path_allowed(path):
            return "Access denied. Path is outside allowed directories."

        p = normalize_path(path)
        if p.exists() and p.is_dir():
            items = [item.name for item in p.iterdir()]
            return ", ".join(items) if items else "Folder is empty."
        return "Folder not found."
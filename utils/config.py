from pathlib import Path
import os

HOME = Path.home()

SAFE_DIRECTORIES = {
    "desktop": HOME / "Desktop",
    "documents": HOME / "OneDrive" / "Documents",
    "downloads": HOME / "Downloads",
    "jarvis": HOME / "Desktop" / "JarvisWorkspace"
}

ALLOWED_TOOLS = {
    "general_chat",
    "scan_large_files",
    "scan_old_files",
    "scan_temp_files",
    "open_youtube",
    "open_spotify",
    "open_linkedin",
    "open_instagram",
    "open_gmail_compose",
    "open_bluetooth_settings",
    "open_display_settings",
    "open_sound_settings",
    "open_wifi_settings",
    "open_file_explorer",
    "open_folder",
    "open_notepad",
    "open_calculator",
    "open_chrome"
}

DANGEROUS_TOOLS = set()
ADMIN_PIN = "1234"
LOG_FILE = os.path.join("logs", "jarvis.log")
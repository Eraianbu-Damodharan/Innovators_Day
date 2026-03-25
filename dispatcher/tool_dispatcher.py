from utils.config import ALLOWED_TOOLS
from chat.general_chat import GeneralChat
from storage_manager.cleanup_manager import CleanupManager
from social_actions.web_actions import WebActions
from settings_control.windows_settings import WindowsSettings
from commands.system_control import SystemControl

class ToolDispatcher:
    def __init__(self):
        self.general_chat = GeneralChat()
        self.cleanup = CleanupManager()
        self.web = WebActions()
        self.settings = WindowsSettings()
        self.system = SystemControl()

    def dispatch(self, tool_data: dict) -> str:
        tool = tool_data.get("tool", "")
        args = tool_data.get("args", {})

        if tool not in ALLOWED_TOOLS:
            return "Blocked. That action is not allowed."

        if tool == "general_chat":
            return self.general_chat.reply(args.get("text", ""))

        if tool == "scan_large_files":
            return self.cleanup.scan_large_files(
                location=args.get("location", "downloads"),
                min_size_mb=int(args.get("min_size_mb", 100))
            )

        if tool == "scan_old_files":
            return self.cleanup.scan_old_files(
                location=args.get("location", "downloads"),
                older_than_days=int(args.get("older_than_days", 90))
            )

        if tool == "scan_temp_files":
            return self.cleanup.scan_temp_files(
                location=args.get("location", "downloads")
            )

        if tool == "open_youtube":
            return self.web.open_youtube(args.get("query", ""))

        if tool == "open_spotify":
            return self.web.open_spotify(args.get("query", ""))

        if tool == "open_linkedin":
            return self.web.open_linkedin()

        if tool == "open_instagram":
            return self.web.open_instagram()

        if tool == "open_gmail_compose":
            return self.web.open_gmail_compose(
                to=args.get("to", ""),
                subject=args.get("subject", ""),
                body=args.get("body", "")
            )

        if tool == "open_bluetooth_settings":
            return self.settings.open_bluetooth_settings()

        if tool == "open_display_settings":
            return self.settings.open_display_settings()

        if tool == "open_sound_settings":
            return self.settings.open_sound_settings()

        if tool == "open_wifi_settings":
            return self.settings.open_wifi_settings()

        if tool == "open_file_explorer":
            return self.system.open_file_explorer()
        
        if tool == "open_folder":
            return self.system.open_folder(args.get("path", ""))

        if tool == "open_notepad":
            return self.system.open_notepad()

        if tool == "open_calculator":
            return self.system.open_calculator()

        if tool == "open_chrome":
            return self.system.open_chrome()

        return "I could not handle that action."
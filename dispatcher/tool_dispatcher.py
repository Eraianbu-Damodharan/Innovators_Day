from utils.config import ALLOWED_TOOLS
from chat.general_chat import GeneralChat
from storage_manager.cleanup_manager import CleanupManager
from social_actions.web_actions import WebActions
from settings_control.windows_settings import WindowsSettings
from commands.system_control import SystemControl
from commands.app_launcher import open_desktop_app, open_web, open_settings


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

        # Web actions
        if tool == "open_youtube":
            query = args.get("query", "").strip()
            if query:
                return open_web(
                    f"https://www.youtube.com/results?search_query={query}",
                    "Opening YouTube"
                )
            return open_web("https://www.youtube.com", "Opening YouTube")

        if tool == "open_spotify":
            query = args.get("query", "").strip()
            if query:
                return open_web(
                    f"https://open.spotify.com/search/{query}",
                    "Opening Spotify"
                )
            return open_web("https://open.spotify.com", "Opening Spotify")

        if tool == "open_linkedin":
            return open_web("https://www.linkedin.com", "Opening LinkedIn")

        if tool == "open_instagram":
            return open_web("https://www.instagram.com", "Opening Instagram")

        if tool == "open_gmail_compose":
            return self.web.open_gmail_compose(
                to=args.get("to", ""),
                subject=args.get("subject", ""),
                body=args.get("body", "")
            )

        # Windows settings
        if tool == "open_bluetooth_settings":
            return self.settings.open_bluetooth_settings()

        if tool == "open_display_settings":
            return self.settings.open_display_settings()

        if tool == "open_sound_settings":
            return self.settings.open_sound_settings()

        if tool == "open_wifi_settings":
            return self.settings.open_wifi_settings()

        # Desktop/system apps
        if tool == "open_file_explorer":
            return open_desktop_app("explorer")

        if tool == "open_folder":
            return self.system.open_folder(args.get("path", ""))

        if tool == "open_notepad":
            return open_desktop_app("notepad")

        if tool == "open_calculator":
            return open_desktop_app("calculator")

        if tool == "open_chrome":
            return open_desktop_app("chrome")

        return "I could not handle that action."
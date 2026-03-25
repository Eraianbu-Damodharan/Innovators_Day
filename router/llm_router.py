import json
import re
from chat.local_llm import LocalLLM

class LLMRouter:
    def __init__(self, llm: LocalLLM):
        self.llm = llm

    def route(self, user_input: str) -> dict:
        text = user_input.strip().lower()

        # ---------- Direct rules for obvious commands ----------
        if text in {"hi", "hello", "hey", "how are you", "who are you"}:
            return {"tool": "general_chat", "args": {"text": user_input}}

        if "open calculator" in text or text == "calculator":
            return {"tool": "open_calculator", "args": {}}

        if "open notepad" in text or text == "notepad":
            return {"tool": "open_notepad", "args": {}}

        if "open chrome" in text or text == "chrome":
            return {"tool": "open_chrome", "args": {}}

        if "open file explorer" in text or "open explorer" in text or text == "file explorer":
            return {"tool": "open_file_explorer", "args": {}}

        if "open bluetooth settings" in text or "bluetooth settings" in text:
            return {"tool": "open_bluetooth_settings", "args": {}}

        if "open display settings" in text or "display settings" in text:
            return {"tool": "open_display_settings", "args": {}}

        if "open sound settings" in text or "sound settings" in text:
            return {"tool": "open_sound_settings", "args": {}}

        if "open wifi settings" in text or "wifi settings" in text or "wi-fi settings" in text:
            return {"tool": "open_wifi_settings", "args": {}}

        if "open linkedin" in text:
            return {"tool": "open_linkedin", "args": {}}

        if "open instagram" in text:
            return {"tool": "open_instagram", "args": {}}

        if "youtube" in text or "play" in text and "youtube" in text:
            query = (
                text.replace("play", "")
                .replace("on youtube", "")
                .replace("youtube", "")
                .strip()
            )
            return {"tool": "open_youtube", "args": {"query": query or "youtube"}}

        if "spotify" in text or ("play" in text and "music" in text):
            query = (
                text.replace("play", "")
                .replace("on spotify", "")
                .replace("spotify", "")
                .strip()
            )
            return {"tool": "open_spotify", "args": {"query": query or "music"}}

        if "large files" in text or "big files" in text:
            location = "downloads"
            if "desktop" in text:
                location = "desktop"
            elif "documents" in text:
                location = "documents"
            return {"tool": "scan_large_files", "args": {"location": location, "min_size_mb": 100}}

        if "old files" in text or "unused files" in text:
            location = "downloads"
            if "desktop" in text:
                location = "desktop"
            elif "documents" in text:
                location = "documents"
            return {"tool": "scan_old_files", "args": {"location": location, "older_than_days": 90}}

        if "temp files" in text or "junk files" in text:
            location = "downloads"
            if "desktop" in text:
                location = "desktop"
            elif "documents" in text:
                location = "documents"
            return {"tool": "scan_temp_files", "args": {"location": location}}
        
        if text.startswith("open folder "):
            folder = user_input[len("open folder "):].strip()
            return {"tool": "open_folder", "args": {"path": folder}}

        if text in {"open documents", "open document folder", "open documents folder"}:
            return {"tool": "open_folder", "args": {"path": "documents"}}

        if text in {"open desktop", "open desktop folder"}:
            return {"tool": "open_folder", "args": {"path": "desktop"}}

        if text in {"open downloads", "open downloads folder"}:
            return {"tool": "open_folder", "args": {"path": "downloads"}}

        if text in {"open jarvis folder", "open jarvis", "open workspace"}:
            return {"tool": "open_folder", "args": {"path": "jarvis"}}

        # ---------- LLM fallback for flexible requests ----------
        prompt = f"""
You are a tool routing assistant for a Jarvis desktop assistant.

Return ONLY valid JSON.
Choose exactly one tool from:
[
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
  "open_notepad",
  "open_calculator",
  "open_chrome"
]

Schema:
{{
  "tool": "tool_name",
  "args": {{}}
}}

User input: {user_input}
"""
        raw = self.llm.ask(prompt).strip()

        try:
            return json.loads(raw)
        except Exception:
            match = re.search(r"\{.*\}", raw, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(0))
                except Exception:
                    pass

        return {"tool": "general_chat", "args": {"text": user_input}}
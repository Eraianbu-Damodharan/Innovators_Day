class GeneralChat:
    def reply(self, text: str) -> str:
        t = text.lower().strip()

        greeting_map = {
            "hi": "Hello! How can I help you?",
            "hello": "Hi! What would you like me to do?",
            "hey": "Hey! How can I assist you?",
            "how are you": "I am functioning well. How can I assist you today?",
            "who are you": "I am your Jarvis assistant. I can help with storage, web actions, settings, and general chat."
        }

        for key, value in greeting_map.items():
            if key in t:
                return value

        return "I can help you manage files, open websites, control settings pages, and chat with you."
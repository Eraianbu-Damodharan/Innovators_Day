from chat.local_llm import LocalLLM
from router.llm_router import LLMRouter
from dispatcher.tool_dispatcher import ToolDispatcher
from utils.logger import log_action
from voice.speech_to_text import SpeechRecognizer
from voice.text_to_speech import speak

# Initialize once so both CLI and Flask can use the same backend
llm = LocalLLM(model="phi3")
router = LLMRouter(llm)
dispatcher = ToolDispatcher()


def handle_text_command(user_text: str) -> str:
    """
    Process a text command from frontend or any other source.
    """
    try:
        spoken_text = user_text.strip().lower()

        if not spoken_text:
            return "Could not understand."

        if spoken_text in {"exit", "quit", "stop"}:
            return "Goodbye."

        tool_data = router.route(spoken_text)
        print("Tool data:", tool_data)

        result = dispatcher.dispatch(tool_data)

        log_action(
            user_input=spoken_text,
            tool=tool_data.get("tool", ""),
            args=str(tool_data.get("args", {})),
            result=result
        )

        return str(result)

    except Exception as e:
        return f"Error: {str(e)}"


def main():
    recognizer = SpeechRecognizer()

    print("Hello. I am your Jarvis assistant.")
    print("Press ENTER to speak, or type 'exit' to quit.\n")

    while True:
        try:
            cmd = input("Press ENTER to speak (or type 'exit'): ").strip().lower()

            if cmd == "exit":
                print("Assistant: Goodbye.")
                break

            spoken_text = recognizer.listen_once().strip().lower()
            print(f"You said: {spoken_text}")

            if not spoken_text:
                print("Assistant: Could not understand.")
                continue

            result = handle_text_command(spoken_text)

            print(f"Assistant: {result}")
            speak(result)

            if spoken_text in {"exit", "quit", "stop"}:
                break

        except KeyboardInterrupt:
            print("\nAssistant: Shutting down.")
            break
        except Exception as e:
            print("Error:", e)
            break


if __name__ == "__main__":
    main()
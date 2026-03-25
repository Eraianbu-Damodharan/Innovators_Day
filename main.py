from chat.local_llm import LocalLLM
from router.llm_router import LLMRouter
from dispatcher.tool_dispatcher import ToolDispatcher
from utils.logger import log_action
from voice.speech_to_text import SpeechRecognizer
from voice.text_to_speech import speak

def main():
    llm = LocalLLM(model="phi3")
    router = LLMRouter(llm)
    dispatcher = ToolDispatcher()
    recognizer = SpeechRecognizer()  # change if needed

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

            if spoken_text in {"exit", "quit", "stop"}:
                print("Assistant: Goodbye.")
                break

            tool_data = router.route(spoken_text)
            print("Tool data:", tool_data)

            result = dispatcher.dispatch(tool_data)

            log_action(
                user_input=spoken_text,
                tool=tool_data.get("tool", ""),
                args=str(tool_data.get("args", {})),
                result=result
            )

            print(f"Assistant: {result}")
            speak(result)

        except KeyboardInterrupt:
            print("\nAssistant: Shutting down.")
            break
        except Exception as e:
            print("Error:", e)
            break

if __name__ == "__main__":
    main()
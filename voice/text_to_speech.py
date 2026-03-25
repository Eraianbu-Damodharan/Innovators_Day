import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 165)

def speak(text: str) -> None:
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
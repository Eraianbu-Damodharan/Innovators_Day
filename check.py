import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    cmd = input("\nPress ENTER to speak (or type 'exit'): ").strip().lower()
    if cmd == "exit":
        break

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError as e:
        print("Speech service error:", e)
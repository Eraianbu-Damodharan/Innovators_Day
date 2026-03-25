import time
import numpy as np
import sounddevice as sd

DEVICE_ID = 1   # your Realtek microphone

def callback(indata, frames, time_info, status):
    if status:
        print("STATUS:", status)

    volume = np.linalg.norm(indata) * 10
    print(f"Mic level: {volume:.4f}")

with sd.InputStream(device=DEVICE_ID, callback=callback, channels=1, samplerate=16000):
    print("Speak now... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped.")
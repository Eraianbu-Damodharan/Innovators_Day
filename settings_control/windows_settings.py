import subprocess

class WindowsSettings:
    def open_bluetooth_settings(self) -> str:
        subprocess.Popen(["start", "ms-settings:bluetooth"], shell=True)
        return "Opened Bluetooth settings."

    def open_display_settings(self) -> str:
        subprocess.Popen(["start", "ms-settings:display"], shell=True)
        return "Opened Display settings."

    def open_sound_settings(self) -> str:
        subprocess.Popen(["start", "ms-settings:sound"], shell=True)
        return "Opened Sound settings."

    def open_wifi_settings(self) -> str:
        subprocess.Popen(["start", "ms-settings:network-wifi"], shell=True)
        return "Opened Wi-Fi settings."
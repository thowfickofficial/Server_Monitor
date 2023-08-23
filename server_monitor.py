import time
import requests
import notify2
from playsound import playsound
import subprocess

# Configure the server URL and notification settings
SERVER_URL = "https://example.com"
CHECK_INTERVAL = 60  # in seconds (1 minute)
SOUND_FILE = "notification_sound.wav"

def send_notification(title, message):
    notify2.init("Server Monitor")
    notification = notify2.Notification(title, message)
    notification.show()

def check_server_status():
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

def main():
    server_status = None

    while True:
        new_status = check_server_status()

        if new_status != server_status:
            if new_status:
                send_notification("Server Status", "Server is now LIVE!")
               
            else:
                send_notification("Server Status", "Server is DOWN!")
                playsound(SOUND_FILE)

            server_status = new_status

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    subprocess.run(["figlet", "Server Monitor"])
    main()

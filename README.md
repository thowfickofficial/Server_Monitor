# Server Monitor

**Server Monitor** is a Python script designed to periodically check the status of a specified server and send notifications when it goes up or down. This tool is useful for keeping track of the availability of critical services or websites.

## Features

- Automatically checks the server status at defined intervals.
- Sends desktop notifications for status changes.
- Optionally plays a notification sound when the server goes down.
- Simple and easy to configure.

## Getting Started

### Prerequisites

Before using Server Monitor, make sure you have the following installed:

- Python 3.x
- Python libraries: `requests`, `notify2`, and `playsound` (you can install them using `pip`).
- A notification sound file (e.g., `notification_sound.wav`).

### Configuration

1. Edit the `SERVER_URL` variable in the script to specify the URL of the server you want to monitor.

         ```python
           SERVER_URL = "https://example.com"
   
2. Adjust the CHECK_INTERVAL variable to set how often the script should check the server status (in seconds).
3. Place your notification sound file (e.g., notification_sound.wav) in the same directory as the script.

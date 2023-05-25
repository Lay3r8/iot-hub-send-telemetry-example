from typing import Final
from os import getenv
from json import dumps as json_dumps
from datetime import datetime
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message
from pytz import timezone as pytz_timezone

# Load environment variables
load_dotenv()
IOT_HUB_CONNECTION_STRING: Final = getenv("IOT_HUB_CONNECTION_STRING")
TIMEZONE: Final = getenv("TIMEZONE", "Europe/Brussels")


def send_message_sync(client, msg):
    print("Sending message...")
    message = Message(msg, content_encoding="utf-8", content_type="application/json")
    client.send_message(message)
    print("Message sent")


def main():
    timezone = pytz_timezone(TIMEZONE)
    current_time = datetime.now(timezone).strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    m = {
        "timestamp": current_time,
        "type": "temperature",
        "value": 17.5
    }
    print("Message to send:")
    print(json_dumps(m, sort_keys=True, indent=2))    
    client = IoTHubDeviceClient.create_from_connection_string(IOT_HUB_CONNECTION_STRING)
    client.connect()
    send_message_sync(client, json_dumps(m).encode("utf-8"))
    client.disconnect()


if __name__ == "__main__":
    main()

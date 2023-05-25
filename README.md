# IoT Hub - Send of telemetry as a device (synchronously)
This example shows how to send telemetry as a device to an IoT Hub using the azure-iot-device SDK for Python. 

## Pre-requisites 
- Python 3+
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
- [Azure IoT extension](https://github.com/Azure/azure-iot-cli-extension#installation) for the Azure CLI


## Installation
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```sh
# Add exec permission to all scripts
chmod +x *.sh

# Monitor events
./azure_connect.sh
./azure_monitor.sh

# Send telemetry
python main.py
```

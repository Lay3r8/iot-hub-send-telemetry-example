#!/bin/bash
source .env

echo "Connecting to IoT Hub $IOT_HUB_NAME in subscription $IOT_HUB_SUBSCRIPTION..."
az account set --subscription $IOT_HUB_SUBSCRIPTION
az iot hub monitor-events --hub-name $IOT_HUB_NAME --output json

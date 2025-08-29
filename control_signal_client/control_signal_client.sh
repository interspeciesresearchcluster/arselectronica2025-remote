#/bin/bash

#!/bin/bash

while :
do
    echo "Starting command..."
    /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/control_signal_client/venv/bin/python /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/control_signal_client/control_signal_client.py
    echo "Command exited, waiting 5 seconds..."
    sleep 5
done
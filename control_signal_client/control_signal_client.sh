#/bin/bash

#!/bin/bash

while :
do
    echo "Command exited, waiting 5 seconds..." >> /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/control_signal_client/control_signal_client.log
    /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/control_signal_client/venv/bin/python /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/control_signal_client/control_signal_client.py >> /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/control_signal_client/control_signal_client.log
    echo "Command exited, waiting 5 seconds..." >> /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/control_signal_client/control_signal_client.log
    sleep 5
done
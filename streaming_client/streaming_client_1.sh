#!/bin/bash

while :
do
    echo "Starting command..." >> /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/streaming_client/streaming_client_1.log
    nc multispeciesresearchcluster.ddnsfree.com 19062 | mpv --no-cache --untimed --no-demuxer-thread  --fs - >> /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/streaming_client/streaming_client_1.log
    echo "Command exited, waiting 5 seconds..." >> /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/streaming_client/streaming_client_1.log
    sleep 5
done
#!/bin/bash

while :
do
    echo "Starting command..." >> /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/streaming_client/streaming_client_2.log
    nc multispeciesresearchcluster.ddnsfree.com 19063 | mpv --no-cache --untimed --no-demuxer-thread  --fs - >> /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/streaming_client/streaming_client_2.log
    echo "Command exited, waiting 5 seconds..." >> /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/streaming_client/streaming_client_2.log
    sleep 5
done
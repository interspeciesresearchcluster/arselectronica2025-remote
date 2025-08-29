#!/bin/bash

while :
do
    nc multispeciesresearchcluster.ddnsfree.com 19062 | mpv --no-cache --untimed --no-demuxer-thread  --fs - >> /home/maxbaraitsersmith/Desktop/arselectronica2025-remote/streaming_client/streaming_client_1.log
    sleep 5
done
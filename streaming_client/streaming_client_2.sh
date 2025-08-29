#!/bin/bash

while :
do
    echo "Starting command..."
    nc multispeciesresearchcluster.ddnsfree.com 19063 | mpv --no-cache --untimed --no-demuxer-thread  --fs -
    echo "Command exited, waiting 5 seconds..."
    sleep 5
done
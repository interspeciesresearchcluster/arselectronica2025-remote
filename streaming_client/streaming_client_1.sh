#!/bin/bash

while :
do
    nc multispeciesresearchcluster.ddnsfree.com 19062 | mpv --no-cache --untimed --no-demuxer-thread  --fs -
    sleep 5
done
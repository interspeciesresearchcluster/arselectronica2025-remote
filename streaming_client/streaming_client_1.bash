#!/bin/bash

FIFO=/tmp/streaming_client_1_pipe

trap cleanup EXIT INT TERM

# Remove the FIFO if it already exists
[[ -p "$FIFO" ]] && rm "$FIFO"
mkfifo "$FIFO"

# Start mpv reading from the FIFO
mpv --no-cache --untimed --no-demuxer-thread  --fs - < "$FIFO" &
MPV_PID=$!

nc multispeciesresearchcluster.ddnsfree.com 19062 > "$FIFO" &
NETCAT_PID=$!

# Wait for ffmpeg to finish
wait $NETCAT_PID

function cleanup {
    echo "Cleaning up..."
    rm "$FIFO"
    kill $MPV_PID 2>/dev/null
    kill $NETCAT_PID 2>/dev/null
}
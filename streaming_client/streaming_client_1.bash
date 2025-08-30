#!/bin/bash

FIFO=/tmp/streaming_client_1_pipe
MPV_PID=""
NETCAT_PID=""

function cleanup {
    echo "Cleaning up processes $MPV_PID, $NETCAT_PID"
    rm "$FIFO"
    kill $MPV_PID 2>/dev/null
    kill $NETCAT_PID 2>/dev/null
}

trap cleanup EXIT INT TERM

# Remove the FIFO if it already exists
[[ -p "$FIFO" ]] && rm "$FIFO"
mkfifo "$FIFO"

# Start mpv reading from the FIFO
mpv --no-cache --untimed --no-demuxer-thread  --fs - < "$FIFO" &
MPV_PID=$!

nc multispeciesresearchcluster.ddnsfree.com 19062 > "$FIFO" &
NETCAT_PID=$!

# Wait for netcat to finish
wait $NETCAT_PID
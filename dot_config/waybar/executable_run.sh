#!/bin/bash
python3 ~/.config/waybar/weather.py &
while true
do
    # echo ""
    out=$(cat ~/.config/hypr/store/dynamic_out.txt)
    echo "$out"  | jq --unbuffered --compact-output
    # cat ~/.config/hypr/scripts/tools/dynamic_out.txt
    sleep 0.5
done
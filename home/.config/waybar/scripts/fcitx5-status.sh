#!/bin/bash

# Get current input method
current_im=$(fcitx5-remote -n)

# Check if fcitx5 is running
if ! pgrep -x "fcitx5" > /dev/null; then
    echo "EN"
    exit 0
fi

# Display appropriate icon/text based on input method
case "$current_im" in
    "keyboard-us")
        echo "EN"
        ;;
    "bamboo")
        echo "VI"
        ;;
    *)
        echo "EN"
        ;;
esac
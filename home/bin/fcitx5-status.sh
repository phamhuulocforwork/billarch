#!/bin/bash

# Script to get current fcitx5 input method status for waybar

get_current_im() {
    # Get current input method from fcitx5
    current_im=$(fcitx5-remote -n 2>/dev/null)
    
    if [ -z "$current_im" ]; then
        echo "EN"
        return
    fi
    
    case "$current_im" in
        "keyboard-us")
            echo "EN"
            ;;
        "bamboo")
            echo "VI"
            ;;
        *)
            # Fallback to first 2 characters of the input method name
            echo "${current_im:0:2}" | tr '[:lower:]' '[:upper:]'
            ;;
    esac
}

get_current_im_full() {
    current_im=$(fcitx5-remote -n 2>/dev/null)
    
    if [ -z "$current_im" ]; then
        echo "English (US)"
        return
    fi
    
    case "$current_im" in
        "keyboard-us")
            echo "English (US)"
            ;;
        "bamboo")
            echo "Vietnamese (Bamboo)"
            ;;
        *)
            echo "$current_im"
            ;;
    esac
}

case "$1" in
    "--status")
        get_current_im
        ;;
    "--full")
        get_current_im_full
        ;;
    "--click")
        # Toggle between input methods
        fcitx5-remote -t
        ;;
    *)
        echo "Usage: $0 [--status|--full|--click]"
        echo "  --status: Show short status (EN/VI)"
        echo "  --full: Show full input method name"
        echo "  --click: Toggle input method"
        ;;
esac
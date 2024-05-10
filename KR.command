#!/bin/zsh

# Function to open a terminal window with specified size and position
function open_terminal_window {
    local script="$1"
    local width="$2"
    local height="$3"
    local x_position="$4"
    local y_position="$5"
    
    osascript -e "tell application \"Terminal\"
        activate
        do script \"$script\"
        delay 1
        set the bounds of the front window to {${x_position}, ${y_position}, ${x_position} + ${width}, ${y_position} + ${height}}
    end tell"
}

# Function to dynamically resize the Tkinter window in BetterMonitr.py
function resize_tkinter_window {
    local script="$1"
    osascript -e "tell application \"Terminal\"
        activate
        do script \"$script\"
    end tell"
}

# Navigate to the Desktop/KR directory
cd ~/Desktop/KR

# Specify the window sizes and positions here
# Example:
open_terminal_window "python3 Desktop/KR/BetterMonitr.py" 800 600 0 0
open_terminal_window "python3 Desktop/KR/UselezSquarez.py" 800 600 900 0
open_terminal_window "python3 Desktop/KR/VisualEnigma.py" 800 600 0 700
open_terminal_window "python3 Desktop/KR/CubEZ.py" 800 600 900 700

# Resize the Tkinter window in BetterMonitr.py based on the terminal window size
resize_tkinter_window "python3 Desktop/KR/BetterMonitr.py"

# Keep the terminal windows open
read -n 1 -s -r -p "Press any key to close this window..."




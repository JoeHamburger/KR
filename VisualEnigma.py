import curses
import time
import random
from curses import wrapper
from random import randint

# Function to print random colored text
def print_random_colored_text(stdscr, text):
    color_pair = random.randint(1, 6)  # Generate a random color pair (1, 2, or 3)
    
    # Define color pairs (Foreground, Background)
    color_pairs = {
        1: (curses.COLOR_GREEN, curses.COLOR_BLACK),
        2: (curses.COLOR_WHITE, curses.COLOR_BLACK),
        3: (curses.COLOR_GREEN, curses.COLOR_WHITE),  # Add more color pairs as needed
        4: (curses.COLOR_BLACK, curses.COLOR_WHITE),
        5: (curses.COLOR_BLACK, curses.COLOR_GREEN),
        6: (curses.COLOR_WHITE, curses.COLOR_GREEN),
    }

    curses.init_pair(color_pair, *color_pairs[color_pair])
    stdscr.attron(curses.color_pair(color_pair))
    stdscr.addstr(text)
    stdscr.attroff(curses.color_pair(color_pair))

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Add 2 extra char before proceeding, use grave to finalize\n")
    player = 0
    array1 = []
    array2 = []
    while player != ord('`'):  # Wait for the backtick key (`) to exit
        player = stdscr.getch()
        if player != curses.ERR:  # Check if getch() returned an actual key
            array1.append(player)
        array2 = array1.copy()  # Create a copy of array1
        arrayavg = int(len(array1) / 4)
        for i in range(0, arrayavg):
            index = random.randint(0, len(array1) - 1)
            array2[index] = random.randint(-arrayavg, arrayavg)
            i += 1
        stdscr.clear()
        for item in array2:
            print_random_colored_text(stdscr, str(item) + " ")
        stdscr.refresh()
    
    if player == ord('`'):
        stdscr.clear()
        for item in array1:
            stdscr.addstr(str(item))
            stdscr.addstr(" ")
        stdscr.refresh()
        stdscr.getch()  # Wait for a key press to exit

if __name__ == "__main__":
    curses.wrapper(main)
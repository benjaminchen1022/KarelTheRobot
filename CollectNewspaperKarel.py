"""
File: CollectNewspaperKarel.py
Name: Benjamin
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code
to guide Karel to walk to the door of its house,
pick up the newspaper (represented by a beeper),
and then return to its original position
in the upper-left corner of the house.
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def main():
    """
    Pre-condition: Karel faces east
    Post-condition: Karel goes back to the initial position and facing east as well
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    # beeper is a symbol of newspaper
    turn_around()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()
    # put the newspaper down


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

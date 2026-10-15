"""
File: StoneMasonKarel.py
Name: Benjamin
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code to guide Karel
to build stone columns that are five beepers tall
on each appropriate avenue, as described in Assignment 1.

Karel should finish on the last avenue at 1st Street, facing east.
"""

from karel.stanfordkarel import *

def turn_around():
    for i in range(2):
        turn_left()

def fix_pillar():
    """
    Pre-condition: Karel is facing east
    Post-condition: Karel is facing north
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()
    turn_around()
    for i in range(4):
        move()

def main():
    """
    Benjamin:
    """
    while front_is_clear():
        if left_is_clear():
            fix_pillar()
            turn_left()
            for i in range(4):
                move()
    fix_pillar()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

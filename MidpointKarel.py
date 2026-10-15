"""
File: MidpointKarel.py
Name: Benjamin
----------------------------
When finished, this program should leave a beeper
on the corner closest to the midpoint of 1st Street.

If 1st Street has an even number of corners,
either of the two central corners is acceptable.
Karel may use additional beepers while searching
for the midpoint, but must remove them before stopping.

The world can be of any size, and you may assume
that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *

def turn_around():
    turn_left()
    turn_left()

def fill_one_line():
    while front_is_clear():
        put_beeper()
        move()
    if not front_is_clear():
        put_beeper()

def go_to_other_end():
    # make sure karel is always on beepers
    while front_is_clear() and on_beeper():
        move()
    if not on_beeper():
        turn_around()
        move()
    else:
        turn_around()

def delete_beeper():
    pick_beeper()
    move()
    while on_beeper():
        go_to_other_end()
        if on_beeper():
            pick_beeper()
            move()
        else:
            move()
    turn_around()
    move()
    put_beeper()

def main():
    fill_one_line()
    turn_around()
    delete_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)

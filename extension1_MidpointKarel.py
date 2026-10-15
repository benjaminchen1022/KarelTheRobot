"""
File: extension1_MidpointKarel.py
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

"""
try to fill the whole square, once karel arrives
to the middle of the square, karel can go down vertically
to the bottom and put an extra beeper. Finally,
reclaim single beepers.
"""

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

def fill_the_outer_square():
    while front_is_clear() and not on_beeper():
        put_beeper()
        move()
        if not front_is_clear() or on_beeper():
            turn_left()
            if on_beeper():
                turn_left()
                move()
                turn_right()
                move()
                if on_beeper() and facing_north():
                    turn_around()

def go_to_bottom():
    while front_is_clear():
        move()
    if not front_is_clear():
        put_beeper()

def go_to_initial_place():
    turn_right()
    while front_is_clear():
        move()
    turn_around()

def reclaim():
    while front_is_clear() and on_beeper():
        pick_beeper()
        move()
        if not front_is_clear() or not on_beeper():
            turn_left()
            if not on_beeper():
                turn_left()
                move()
                turn_right()
                move()
                if not on_beeper() and facing_north():
                    turn_around()
            # at the end, keep karel facing south

def finish():
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_left()

def main():
    fill_the_outer_square()
    go_to_bottom()
    go_to_initial_place()
    reclaim()
    finish()
    # I'm not sure whether it's acceptable or not if my karel is above the beeper
    # I believe there's gonna be a better way to write this code, but my little brain is tapped out:((

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)

"""
File: CheckerboardKarel.py
Name: Benjamin
----------------------------
When finished, this program should
draw a checkerboard pattern using
beepers, as described in Assignment 1.

The solution should work correctly
for all of the sample worlds provided
in the starter folder.
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def fill_the_line():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def main():
    fill_the_line()
    turn_left()
    while front_is_clear():
        if not on_beeper():
            move()
            turn_left()
            fill_the_line()
        else:
            move()
            turn_left()
            move()
            fill_the_line()
        turn_right()
        if front_is_clear():
            move()
            turn_right()
            fill_the_line()
            turn_left()
        else:
            turn_left()





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

from pyautogui import position, moveTo
from random import randint
from screeninfo import get_monitors
from time import sleep

print("How many minutes would you like to keep your computer active")
while True:
    try:
        user_input = int(input())
        if user_input:
            break
    except ValueError:
        print("Program takes only full number values\n"
              "try again: ")

"Time counted for later loop usage in every 2 seconds rounds"
counted_time = (user_input * 60) / 2

for i in get_monitors():
    """Get only X and Y values from Monitor Class"""
    screen_width = i.width
    screen_height = i.height

for j in range(int(counted_time)):
    """Choose random X and Y positions and actual cursor position to use it in later comparison"""
    cursor_value_x = randint(1, screen_width)
    cursor_value_y = randint(1, screen_height)
    actual_cursor_position = position()

    if cursor_value_x != actual_cursor_position[0] and cursor_value_y != actual_cursor_position[1]:
        moveTo(cursor_value_x, cursor_value_y, 0.5)
        sleep(2)
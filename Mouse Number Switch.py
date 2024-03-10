import keyboard
from pynput.mouse import Listener
import time

current_number = 9
# The numbers to cycle through
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Last time a tilt event was handled
last_tilt_time = 0
# Minimum time (in seconds) between two consecutive tilt events
min_tilt_interval = 0.15

# This function will be called every time the mouse is tilted or the mouse wheel is clicked
def on_tilt(x, y, dx, dy):
    global current_number, last_tilt_time
    if time.time() - last_tilt_time < min_tilt_interval:
        # Ignore the event if it's too soon after the previous one
        return
    last_tilt_time = time.time()
    
    if abs(dx) > abs(dy):
        if dx > 0:
            # Tilted to the right, move to the next number
            current_number = (current_number + 1) % len(numbers)
        elif dx < 0:
            # Tilted to the left, move to the previous number
            current_number = (current_number - 1) % len(numbers)
        keyboard.press_and_release(str(numbers[current_number]))
        print_num = current_number + 1
        if print_num == 10:
            print("You are on number: 0", end="\r")
        else:
            print("You are on number:", print_num, end="\r")

def on_click(x, y, button, pressed):
    if button == button.middle and pressed:
        # Simulate a key press and release of the current number
        keyboard.press_and_release(str(numbers[current_number]))

# Start listening for mouse events
with Listener(on_scroll=on_tilt, on_click=on_click) as listener:
    listener.join()
"""
This module contains the main event loop for an auto-clicker program. It includes
functions to handle key press events and to control the auto-clicking behavior based
on these events.
"""

import time

import keyboard
import mouse
from constants import AUTO_CLICK_KEY, TOGGLE_LISTENER_KEY

# Initialize variables
AUTO_CLICKING = False
LISTENER = True


# Function to handle the 'c' key press event
def on_press(event):
    """
    Handle the 'c' key press event. Toggles the auto-clicking state.

    Parameters:
    event (keyboard.KeyboardEvent): The event that triggered the function call.
    """
    global AUTO_CLICKING  # pylint: disable=W0603
    if event.name == AUTO_CLICK_KEY:
        AUTO_CLICKING = not AUTO_CLICKING
        print("Auto-clicking:", "On" if AUTO_CLICKING else "Off")


# Main custom event loop function for auto-clicking
def custom_event_loop(cps):
    """
    Main custom event loop for auto-clicking. Performs a mouse click and sleeps
    for the specified CPS interval if auto-clicking is enabled. Checks for the
    stop signal (pressing the 'q' key) and toggles the listener state.

    Parameters:
    cps (float): The time interval between clicks.
    """
    global AUTO_CLICKING, LISTENER  # pylint: disable=W0602
    while True:
        if (
            AUTO_CLICKING
        ):  # Perform a mouse click and sleep for the specified CPS interval
            mouse.click("left")
            time.sleep(cps)

        if keyboard.is_pressed(
            TOGGLE_LISTENER_KEY
        ):  # Check for stop signal (for example, pressing the "q" key)
            if LISTENER:
                keyboard.unhook_all()
            else:
                keyboard.on_press(
                    on_press
                )  # Toggle the listener state and print status
            LISTENER = not LISTENER
            print("Listener:", "On" if LISTENER else "Off")
            time.sleep(0.5)

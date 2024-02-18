"""
This module is the main entry point for the auto-clicker program. It gets the
desired clicks per second (CPS) speed from the user, calculates the time interval
between clicks based on the desired CPS, and starts the key press listener and
the custom event loop for auto-clicking.
"""

import keyboard
from constants import AUTO_CLICK_KEY, TOGGLE_LISTENER_KEY
from events.event_loop import on_press, custom_event_loop
from events.user_input import get_user_cps
from utils.cps_calculator import calculate_cps_speed

if __name__ == "__main__":
    user_cps = get_user_cps()  # Get the desired CPS speed from the user
    cps = calculate_cps_speed(
        user_cps
    )  # Calculate the time interval between clicks based on desired CPS

    # Display instructions and default keybinds
    print(
        f'\nIMPORTANT!!! Default keybinds are set to "{AUTO_CLICK_KEY}" for the auto '
        f'clicker and "{TOGGLE_LISTENER_KEY}" for the listener.'
    )
    print(
        "The listener is automatically enabled and is used for detecting the key "
        "press for the auto clicker."
    )
    print("You may change these keybinds in the file yourself if you would like to.\n")

    keyboard.on_press(on_press)  # Start the on_press listener
    custom_event_loop(cps)  # Start the custom event loop for auto-clicking

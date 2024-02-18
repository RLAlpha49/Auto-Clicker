"""
This module contains a function to calculate the time interval between clicks
based on the desired clicks per second (CPS) rate provided by the user.
"""


# Function to calculate the time interval between clicks based on desired CPS
def calculate_cps_speed(user_cps):
    """
    Calculate the time interval between clicks based on the desired CPS rate.

    Parameters:
    user_cps (int): The desired clicks per second rate.

    Returns:
    float: The time interval between clicks.
    """
    set_speed = 1 / user_cps
    print(
        f"Speed set to {user_cps} CPS. Time between clicks: {set_speed:.4f}"
    )  # Display the set CPS speed and time interval
    return set_speed

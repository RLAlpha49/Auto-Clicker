"""
This module contains a function to get the desired clicks per second (CPS) speed 
from the user. The user can choose from a list of preset options or enter a custom 
CPS speed.
"""

from utils.presets import Presets


# Function to get the desired clicks per second (CPS) speed from the user
def get_user_cps():
    """
    Get the desired clicks per second (CPS) speed from the user. The user can
    choose from a list of preset options or enter a custom CPS speed.

    Returns:
    int: The desired CPS speed.
    """
    print("Choose a CPS option:")
    for option in Presets:
        print(f"{option.name[-1]}. {option.value} CPS")

    while True:
        choice = input("Enter your choice (1-5) or '6' for Custom: ")

        if choice == "6":
            # Custom option: Get user input for desired CPS speed
            while True:
                try:
                    user_cps = int(
                        input("Enter Desired CPS(Clicks Per Second) Speed (1 - 1000): ")
                    )
                    if 1 <= user_cps <= 1000:
                        return user_cps
                    print("Value must be between 1 and 1000!")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif int(choice) in range(1, 6):  # Use the selected preset option
            return Presets[f"OPTION_{choice}"].value
        else:
            print("Invalid choice. Please choose a valid option (1-6).")

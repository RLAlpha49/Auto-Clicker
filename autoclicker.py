import keyboard
import time
import mouse

'''
###############################################################
DISCLAIMER: If you choose to set the CPS to a higher value than
my 1000 limit, then you need to get rid of the "cps = cps_speed()"
function in the main program. As well as take out the "cps"
parameter from the 'custom_event_loop' function. Lastly, you would 
need to switch the 'cps' variable in "time.sleep(cps)" to your
desired cps. Note that it needs to be in seconds. For example,
"0.001" for 1000 CPS and "0.0001" for 10000 CPS.

I Chose the limit of 1000 because, at some point, programs just
don't accept more clicks. Websites, especially, lag or freeze a lot.
when going fast.
###############################################################
'''

# Initialize variables
auto_clicking = False
listener = True

# Function to set the desired clicks per second (CPS) speed
def cps_speed():
    presets = {
        '1': 50, '2': 100, '3': 250, '4': 500, '5': 1000
    }

    print("Choose a CPS option:")
    for key, value in presets.items():
        print(f"{key}. {value} CPS")

    while True:
        choice = input("Enter your choice (1-5) or '6' for Custom: ")

        if choice == '6':
            # Custom option: Get user input for desired CPS speed
            while True:
                user_cps = input("Enter Desired CPS(Clicks Per Second) Speed (1 - 1000): ")
                if 1 <= int(user_cps) <= 1000:
                    break
                else:
                    print("Value must be between 1 and 1000!")
            set_speed = 1 / int(user_cps)  # Calculate the time interval between clicks based on desired CPS
            break
        elif choice in presets:  # Use the selected preset option
            user_cps = presets[choice]
            set_speed = 1 / user_cps
            break
        else:
            print("Invalid choice. Please choose a valid option (1-6).")

    print(f'Speed set to {user_cps} CPS. Time between clicks: {set_speed:.4f}')  # Display the set CPS speed and time interval
    return set_speed


# Function to handle the 'c' key press event
def on_press(event):
    global auto_clicking
    if event.name == 'c':
        auto_clicking = not auto_clicking
        print('Auto-clicking:', 'On' if auto_clicking else 'Off')

# Main custom event loop function for auto-clicking
def custom_event_loop(cps):
    global auto_clicking, listener
    while True:
        if auto_clicking: # Perform a mouse click and sleep for the specified CPS interval
            mouse.click('left')
            time.sleep(cps)

        if keyboard.is_pressed('q'): # Check for stop signal (for example, pressing the "q" key)
            keyboard.unhook_all() if listener else keyboard.on_press(on_press) # Toggle the listener state and print status
            listener = not listener
            print('Listener:', 'On' if listener else 'Off')
            time.sleep(0.5)

if __name__ == "__main__":
    cps = cps_speed() # Get the desired CPS speed from the user
    
    # Display instructions and default keybinds
    print('\nIMPORTANT!!! Default keybinds are set to "c" for the auto clicker and "q" for the listener.')
    print('The listener is automatically enabled and is used for detecting the key press for the auto clicker.')
    print('You may change these keybinds in the file yourself if you would like to.\n')
    
    keyboard.on_press(on_press) # Start the on_press listener
    custom_event_loop(cps) # Start the custom event loop for auto-clicking

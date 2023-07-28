import keyboard
import time
import mouse

###############################################################
'''
DISCLAIMER: If you choose to set the CPS to a higher value than
my 1000 limit, then you need to get rid of the "cps = cps_speed()"
function in the main program. As well as take out the "cps"
parameter from the 'custom_event_loop' function. Lastly, you would 
need to switch the 'cps' variable in "time.sleep(cps)" to your
desired cps. Note that it needs to be in seconds. For example,
"0.001" for 1000 CPS and "0.0001" for 10000 CPS.

I Chose the limit of 1000 because, at some point, programs just
don't accept more clicks. Websites especially, lag or freeze a lot.
when going fast.
'''
###############################################################

# Initialize variables
auto_clicking = False
listener = True

# Function to set the desired clicks per second (CPS) speed
def cps_speed():
    # Get user input for desired CPS speed
    user_cps = input("Enter Desired CPS(Clicks Per Second) Speed (1 - 1000): ")
    
    # Check if the user input is within the valid range (1 - 1000)
    while int(user_cps) > 1000 or int(user_cps) < 1:
        print("Value must be between 1 and 1000!")
        user_cps = input("Enter Desired CPS(Clicks Per Second) Speed (1 - 1000): ")
    
    # Calculate the time interval between clicks based on desired CPS
    set_speed = 1 / int(user_cps)
    print('Speed set to ' + user_cps + ' CPS. Time between clicks: ' + str(set_speed))
    return set_speed

# Function to handle the 'c' key press event
def on_press(event):
    global auto_clicking
    if event.name == 'c':
        auto_clicking = not auto_clicking
        print('Auto-clicking:', 'On' if auto_clicking else 'Off')

# Main custom event loop function for auto-clicking
def custom_event_loop(cps):
    global auto_clicking, listener  # Declare auto_clicking and listener as global inside the function
    while True:
        if auto_clicking:
            # Perform a mouse click and sleep for the specified CPS interval
            mouse.click('left')
            time.sleep(cps)

        # Check for stop signal (for example, pressing the "q" key)
        if keyboard.is_pressed('q'):
            if listener is True:
                # If listener is on, turn it off and print status
                keyboard.unhook_all()  # Unhook the previous listener
                listener = False
                print('Listener:', 'Off')
                time.sleep(0.5)
            else:
                # If listener is off, turn it on and print status
                keyboard.on_press(on_press)
                listener = True  # Re-enable the listener when pressing 'q'
                print('Listener:', 'On')
                time.sleep(0.5)

if __name__ == "__main__":
    # Get the desired CPS speed from the user
    cps = cps_speed()
    
    print('\nIMPORTANT!!! Default keybinds are set to "c" for the auto clicker and "q" for the listener.')
    print('The listener is automatically enabled and is used for detecting the key press for the auto clicker.')
    print('You may change these keybinds in the file yourself if you would like to.\n')
    
    # Start the on_press listener
    keyboard.on_press(on_press)
    
    # Start the custom event loop for auto-clicking
    custom_event_loop(cps)

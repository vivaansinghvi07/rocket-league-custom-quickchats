from inputs import get_gamepad                  # for detecting controller on your computer

# INSTRUCTIONS: Run this, with your controller connected,
# and press your dpad buttons, and the program will spit our what they are called.
# When the program outputs their codes, enter them in main.py under the X and Y constants

def test():                                     
    while True:                                 
        events = get_gamepad()
        for event in events:
            print(event.code)       # prints the code of a pressed button

test()
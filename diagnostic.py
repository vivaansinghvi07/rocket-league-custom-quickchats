# allows for library download outside of OS
import sys
import subprocess

# download libaries needed
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'inputs'])

from inputs import get_gamepad                  # for detecting controller on your computer

"""
INSTRUCTIONS: Run this, with your controller connected, and
press your dpad buttons, and the program will spit out what
what they are called. When the program outputs their codes,
use them as directed by the README file on GitHub. Keep the 
fact that there will be only two different codes: an X (for 
left-right) and a Y (for up-down) in mind. To terminate this 
process, close theTerminal window or press Ctrl+C.
""" 

# runs diagnostic test
def test():                                     
    while True:                                 
        events = get_gamepad()
        for event in events:
            if event.code.strip() != "SYN_REPORT":
                print("Code: " + event.code.strip()) # prints the code of a pressed button
test()

# To terminate, press Ctrl+C
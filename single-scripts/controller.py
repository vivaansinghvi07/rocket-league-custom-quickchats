class Chat():
    ### EDIT QUICKCHATS HERE                        # THE COMBINATIONS FOR THE CHATS ARE SHOWN HERE:
    quickchats = [["Quickchat Placeholder",         # controller: up - up           
                   "Quickchat Placeholder",         # controller: up - left         
                   "Quickchat Placeholder",         # controller: up - down         
                   "Quickchat Placeholder"],        # controller: up - right        
                  ["Quickchat Placeholder",         # controller: left - up         
                   "Quickchat Placeholder",         # controller: left - left       
                   "Quickchat Placeholder",         # controller: left - down       
                   "Quickchat Placeholder"],        # controller: left - right      
                  ["Quickchat Placeholder",         # controller: down - up         
                   "Quickchat Placeholder",         # controller: down - left       
                   "Quickchat Placeholder",         # controller: down - down       
                   "Quickchat Placeholder"],        # controller: down - right      
                  ["Quickchat Placeholder",         # controller: right - up        
                   "Quickchat Placeholder",         # controller: right - left      
                   "Quickchat Placeholder",         # controller: right - down      
                   "Quickchat Placeholder"]]        # controller: right - right     
    
    # EDIT KEYBOARD CHAT BIND HERE
    chatbind = 't'

    # EDIT DPADS HERE
    dpad_x = "ABS_HAT0X"    # LEFT-RIGHT
    dpad_y = "ABS_HAT0Y"    # UP-DOWN


# allows for importing of needed libaries
import sys
import subprocess

# download libaries needed
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'inputs'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'time'])

from inputs import get_gamepad                  # for detecting controller on your computer
from pynput.keyboard import Key, Controller     # for sending text
import time

def getPrompt(store, number, quickchats):
    return quickchats[store-1][number-1]        # returns the corresponding quickchat

def printPrompt(keyboard, prompt, chatbind):

    # presses the chat binding
    keyboard.press(chatbind)
    keyboard.release(chatbind)

    # waits a little to make it work
    time.sleep(0.01)

    # presses every letter
    for letter in prompt:
        if letter.isupper():
            with keyboard.pressed(Key.shift):             # if the letter is uppercase, hold shift while doing it
                keyboard.press(letter.lower())
                keyboard.release(letter.lower())
        else:                                           # otherwise print as normal
            keyboard.press(letter)
            keyboard.release(letter)
            
    # sends chat
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

DPADX = Chat.dpad_x                 # code for left-right dpad
DPADY = Chat.dpad_y                 # code for up-down dpad
CHATBIND = Chat.chatbind            # your rocket league chat binding
QUICKCHATS = Chat.quickchats        # the quickchats used

def main():

    # stores values - used later on
    waitForAnother = False      # defines if we need to wait for another input to enter a chat
    store = -1                  # stores the input that you pressed, so you can chat with 2 inputs

    # this controls your keyboard
    keyboard = Controller()

    # runs program for as long as you let it - pres sCtrl 
    while True:

        # gets the gamepad plugged in
        events = get_gamepad()

        # goes for each event
        for event in events:

            # checks for d-pad button press
            if (event.code.strip() == DPADX or event.code.strip() == DPADY) and event.state != 0:

                # makes it so that you need to click two dpads to send a chat
                waitForAnother = not waitForAnother

                # gets the code (for making chats unique)
                code = 1 if event.code.strip() == DPADX else 0
                
                # creates nums from 1, 2, 3, 4 (state can be -1 a or 1)
                number = event.state + 2 + code     # 1: up, 2: left, 3: down, 4: right

                if waitForAnother:      
                    store = number      # if we need to wait for another update the stored value to the number
                else:                   
                    printPrompt(keyboard, getPrompt(store, number, QUICKCHATS), CHATBIND)     # otherwise, print the chat

# runs the program
main()
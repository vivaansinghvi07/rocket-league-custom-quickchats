from inputs import get_gamepad                  # for detecting controller on your computer
from pynput.keyboard import Key, Controller     # for sending text
from settings import Chat
import time

DPADX = Chat.dpad_x                 # code for left-right dpad
DPADY = Chat.dpad_y                 # code for up-down dpad
CHATBIND = Chat.chatbind            # your rocket league chat binding
QUICKCHATS = Chat.quickchats        # the quickchats used

def getPrompt(store, number, quickchats):
    return quickchats[store-1][number-1]        # returns the corresponding quickchat

def printPrompt(keyboard, prompt):

    # presses the chat binding
    keyboard.press(CHATBIND)
    keyboard.release(CHATBIND)

    # waits a little to make it work
    time.sleep(0.01)

    # presses every letter
    for letter in prompt:
        if letter.isupper():
            with keyboard.press(Key.shift):             # if the letter is uppercase, hold shift while doing it
                keyboard.press(letter.lower())
                keyboard.release(letter.lower())
        else:                                           # otherwise print as normal
            keyboard.press(letter)
            keyboard.release(letter)
            
    # sends chat
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def main():

    # stores values - used later on
    waitForAnother = False      # defines if we need to wait for another input to enter a chat
    store = -1                  # stores the input that you pressed, so you can chat with 2 inputs

    # this controls your keybaord
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
                    printPrompt(keyboard, getPrompt(store, number, QUICKCHATS))     # otherwise, print the chat

# runs the program
main()
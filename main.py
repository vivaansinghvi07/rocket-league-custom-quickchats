from inputs import get_gamepad                  # for detecting controller on your computer
from pynput.keyboard import Key, Controller     # for sending text
from prompts import Chat
import time

DPADX = "ABS_HAT0X"                 # codes for d-pads
DPADY = "ABS_HAT0Y"
CHATBIND = "t"                      # your rocket league chat binding
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

    # stores values
    waitForAnother = False
    store = -1

    # creates a keybaord object
    keyboard = Controller()
    while True:

        # gets the gamepad plugged in
        events = get_gamepad()

        # goes for each event
        for event in events:

            # if its a dpad event (for quickchats)
            if (event.code.strip() == DPADX or event.code.strip() == DPADY) and event.state != 0:

                # makes it so that you need to click two dpads to send a chat
                waitForAnother = not waitForAnother

                # gets the code (for making chats unique)
                code = 1 if event.code.strip() == DPADX else 0
                
                # creates nums from 1, 2, 3, 4 (state can be -1 a or 1)
                number = event.state + 2 + code         

                if waitForAnother:          # if we need to wait for another update the stored value to the number
                    store = number
                else:                       # otherwise, print the chat
                    printPrompt(keyboard, getPrompt(store, number, QUICKCHATS))


if __name__ == "__main__":
    main()
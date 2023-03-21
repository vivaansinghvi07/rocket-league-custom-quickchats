class Chat():
    ### EDIT QUICKCHATS HERE                        # THE COMBINATIONS FOR THE CHATS ARE SHOWN HERE:
    quickchats = [["Quickchat Placeholder",         # kbm: 1 - 1
                   "Quickchat Placeholder",         # kbm: 1 - 2
                   "Quickchat Placeholder",         # kbm: 1 - 3
                   "Quickchat Placeholder"],        # kbm: 1 - 4
                  ["Quickchat Placeholder",         # kbm: 2 - 1
                   "Quickchat Placeholder",         # kbm: 2 - 2
                   "Quickchat Placeholder",         # kbm: 2 - 3        ****************
                   "Quickchat Placeholder"],        # kbm: 2 - 4        NOTE: NO NUMBERS
                  ["Quickchat Placeholder",         # kbm: 3 - 1        ****************
                   "Quickchat Placeholder",         # kbm: 3 - 2
                   "Quickchat Placeholder",         # kbm: 3 - 3
                   "Quickchat Placeholder"],        # kbm: 3 - 4
                  ["Quickchat Placeholder",         # kbm: 4 - 1
                   "Quickchat Placeholder",         # kbm: 4 - 2
                   "Quickchat Placeholder",         # kbm: 4 - 3
                   "Quickchat Placeholder"]]        # kbm: 4 - 4
    
    # EDIT KEYBOARD CHAT BIND HERE
    chatbind = 't'

    # EDIT DPADS HERE
    dpad_x = "ABS_HAT0X"    # LEFT-RIGHT
    dpad_y = "ABS_HAT0Y"    # UP-DOWN

# allows for importing of needed libaries
import sys
import subprocess

# download libaries needed
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'time'])

from pynput.keyboard import Controller, Listener, Key       # imports keyboard listening and the keyboard controller
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

class KbmQuickchat():

    # gets the constants
    QUICKCHATS = Chat.quickchats        # the quickchats
    CHATBIND = Chat.chatbind            # the chatbind (usually t)

    def __init__(self):

        # starter values
        self.store = -1
        self.waitForAnother = False

        # gets the keyboard for output
        self.keyboard = Controller()

    def on_press(self, key):
        try:
            if key.char in ['1', '2', '3', '4']:       # only detects for 1, 2, 3, 4

                # toggles storage
                self.waitForAnother = not self.waitForAnother

                # if we need to store a number, do it
                if self.waitForAnother:
                    self.store = int(key.char)
                else:
                    printPrompt(self.keyboard, getPrompt(self.store, int(key.char), KbmQuickchat.QUICKCHATS), KbmQuickchat.CHATBIND)    # prints quickchat
        except:
            if key == Key.esc:          # terminates program
                raise KeyboardInterrupt
            return

    def run(self):
        with Listener(on_press=self.on_press) as listener:      # listens to every key press
            listener.join()
    
# runs the thing
chat = KbmQuickchat()
chat.run()
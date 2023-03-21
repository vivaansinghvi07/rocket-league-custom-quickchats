from pynput.keyboard import Controller, Listener, Key       # imports keyboard listening and the keyboard controller
from printer import getPrompt, printPrompt          # gets quickchat printing methods
from settings import Chat

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
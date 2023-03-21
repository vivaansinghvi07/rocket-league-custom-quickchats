from pynput.keyboard import Events, Controller, Listener, Key        # imports keyboard listening and the keyboard controller
from printer import getPrompt, printPrompt          # gets quickchat printing methods
from settings import Chat 

class KbmQuickchat():

    # gets the constants
    QUICKCHATS = Chat.quickchats        # the quickchats
    CHATBIND = Chat.chatbind            # the chatbind (usually t)

    def __init__(self):
        self.store = -1
        self.waitForAnother = False
        self.keyboard = Controller()

    def on_press(self, key):
        print(key)
        try:
            if key.char in ['1', '2', '3', '4']:       # only detects for 1, 2, 3, 4
                self.waitForAnother = not self.waitForAnother
                if self.waitForAnother:
                    self.store = int(key.char)
                else:
                    printPrompt(self.keyboard, getPrompt(self.store, int(key.char), KbmQuickchat.QUICKCHATS), KbmQuickchat.CHATBIND)    # prints quickchat
        except:
            return

    def run(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
    
chat = KbmQuickchat()
chat.run()
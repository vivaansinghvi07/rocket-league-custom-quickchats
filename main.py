from inputs import get_gamepad
from pynput.keyboard import Key, Controller
import time

def getPrompt(store, number):
    prompts = [["Amazing shot!!",
               "I'm the greatest!",
               "let me cook",
               "go for the fricking ball"],
               ["sorry my bad whoopsies",
               "no problemo",
               "outta boost bro",
               "my fault dawg"],
               ["what a save",
               "quickchat placeholder 1",
               "quickchat placeholder 2",
               "vroom vroom"],
               ["car ball",
               "this is rokt leeg",
               "hi",
               "good game"]]
    
    return prompts[store-1][number-1]

def printPrompt(keyboard, prompt):
    keyboard.press('t')
    keyboard.release('t')
    time.sleep(0.01)
    for letter in prompt:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def main():
    waitForAnother = False
    store = -1
    keyboard = Controller()
    while 1:
        events = get_gamepad()
        for event in events:
            if (event.code.strip() == "ABS_HAT0X" or event.code.strip() == "ABS_HAT0Y") and event.state != 0:
                waitForAnother = not waitForAnother
                code = 1 if event.code.strip() == "ABS_HAT0X" else 0
                number = event.state + 2 + code         # creates nums from 1, 2, 3, 4
                if waitForAnother:
                    store = number
                else:
                    printPrompt(keyboard, getPrompt(store, number))


if __name__ == "__main__":
    main()
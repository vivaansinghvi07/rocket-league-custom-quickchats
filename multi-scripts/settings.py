class Chat():
    ### EDIT QUICKCHATS HERE                        # THE COMBINATIONS FOR THE CHATS ARE SHOWN HERE: BOTH KBM AND CONTROLLER
    quickchats = [["let me cook",         # controller: up - up           kbm: 1 - 1
                   "i'm the best",         # controller: up - left         kbm: 1 - 2
                   "you guys suck!",         # controller: up - down         kbm: 1 - 3
                   "hit the ball!"],        # controller: up - right        kbm: 1 - 4
                  ["amazing shot!!!!",         # controller: left - up         kbm: 2 - 1
                   "nice pass",         # controller: left - left       kbm: 2 - 2
                   "WHAT A SAVE!!",         # controller: left - down       kbm: 2 - 3
                   "thank you so much"],        # controller: left - right      kbm: 2 - 4
                  ["i meant to do that",         # controller: down - up         kbm: 3 - 1
                   "no problemo",         # controller: down - left       kbm: 3 - 2
                   "sorry my bad",         # controller: down - down       kbm: 3 - 3
                   "whoopsies!"],        # controller: down - right      kbm: 3 - 4
                  ["NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",         # controller: right - up        kbm: 4 - 1
                   "this is rokt leeg!",         # controller: right - left      kbm: 4 - 2
                   "demoing",         # controller: right - down      kbm: 4 - 3
                   "passing"]]        # controller: right - right     kbm: 4 - 4
    
    # EDIT KEYBOARD CHAT BIND HERE
    chatbind = 't'

    # EDIT DPADS HERE
    dpad_x = "ABS_HAT0X"    # LEFT-RIGHT
    dpad_y = "ABS_HAT0Y"    # UP-DOWN
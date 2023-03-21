# rocket-league-custom-quickchats
Custom Quickchats for the video game Rocket League!

## Requirements:
- Windows OS (which Rocket League generally runs on anyways)
  - Other operating systems have not been tested.
- [XBox Controller](https://www.bestbuy.com/site/microsoft-xbox-wireless-controller-for-xbox-series-x-xbox-series-s-xbox-one-windows-devices-pulse-red/6448932.p?skuId=6448932#anchor=productVariations)
  - Not tested with PlayStation or another brand
  
## Usage:
- All edits you should need to do are in `settings.py`
  - Edit your quickchats: search for the `EDIT QUICKCHATS HERE` comment
  - If controller: Get the codes for your d-pads with `diagnostic.py`
    - If they are different, change them by searching for the `EDIT DPADS HERE` comment
  - If KBM: your quickchats MUST NOT HAVE NUMBERS IN THEM:
    - Also, make sure your quickchats are bound to the numbers 1-4 (the Rocket League defaults) on your keyboard
  - Make sure your chat bind is accurate - if its not `t`, change it where it says `EDIT KEYBOARD CHAT BIND HERE`
- Run the script in the background, read the directions on were the quickchats are in `settings.py`, and enjoy!
  - If you're on KBM, run `kbm.py`.
  - If you're on controller, run `controller.py`

Here are the chats being used in-game!

![Example](example.png)
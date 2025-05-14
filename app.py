import pywhatkit
import pyautogui
import time


# Send the message (this only opens the tab and types the message)
pywhatkit.sendwhatmsg("+919883850357", "Hello from my local machine!", 23, 18)

# Wait a bit before sending
time.sleep(20)

# Press Enter to send the message
pyautogui.press('enter')
#message bomber v1 by snpsujon
#a simple python script
#visit : https://snpsujon.me
#github : https://github.com/snpsujon



import pyautogui
import time

limit = input("How many message you want to send : ")
message = raw_input("Your Message: ")

while limit > 0:
    time.sleep(2)
    pyautogui.typewrite( message)
    pyautogui.press('enter')
    limit = limit - 1

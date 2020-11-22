#message bomber v1 by snpsujon
#a simple python script
#visit : https://snpsujon.me
#github : https://github.com/snpsujon

#Firstly you need to install pyautogui type following command pip install pyautogui

import pyautogui
import time

limit = input("How many message you want to send : ")
message = raw_input("Your Message: ")

while limit > 0:
    time.sleep(2) #For Time interval
    pyautogui.typewrite(message)  #Your message 
    pyautogui.press('enter')  #auto press from keyboard
    limit = limit - 1  #loop decriment

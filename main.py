import pyautogui
from time import sleep
from colorama import Fore

pyautogui.FAILSAFE = False

print(Fore.CYAN+"""
  __  __    _    ____ ____   ___  
 |  \/  |  / \  / ___|  _ \ / _ \ 
 | |\/| | / _ \| |   | |_) | | | |
 | |  | |/ ___ \ |___|  _ <| |_| |
 |_|  |_/_/   \_\____|_| \_|\___/ 
""")
print(Fore.GREEN+"[1] Typewrite")
print(Fore.GREEN+"[2] Keybinds")
inputField = input("Please select an option: \n")
s = input(Fore.BLUE+"Enter your message: ")
x = input(Fore.BLUE+"How many times: ")
t = input(Fore.BLUE+"Countdown: ")
d = input(Fore.BLUE+"Delay per message: ")
howManyX = int(x)
tMinus = int(t)
delay = int(d)
while(tMinus != 0):
    print("T-Minus "+str(tMinus))
    sleep(1)
    tMinus -= 1
if inputField == "1":
      for i in range(0, howManyX):
        pyautogui.typewrite(s)
        pyautogui.typewrite("\n")
        sleep(delay)

if inputField == "2":
  confirm = input(Fore.YELLOW+"Have you copied the text? If not, copy it, then come back.")
    if confirm != "y" and confirm != "yes":
        exit()
      for i in range(0, howManyX):
        pyautogui.hotkey("ctrl","v")
        pyautogui.typewrite("\n")
        sleep(delay)

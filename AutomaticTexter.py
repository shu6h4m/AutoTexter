from colorama import init
init()
from colorama import Fore, Back, Style
import pyautogui
import time
print("\n\n\n------------------------------------------------------")
print()
print(Fore.GREEN + "  *** A Software Created by shubham in Python ***")
print(Style.RESET_ALL)
print('------------------------------------------------------')
print()
print(Fore.RED + "Step 1 : Just Paste or Write Your Text Below")
print("Step 2 : Go Where You Want to Type This Automatically.")
print(Style.RESET_ALL)
print("------------------------------------------------------")
print("\n")
text = input("Enter Or Paste Your Text Here : ")
shubham = input("Enter Delay Time in Seconds : ")
print("Your Text will be Sent Automatically After "+shubham+" Seconds")
shubham = int(shubham)
time.sleep(shubham)
pyautogui.typewrite(text + "\n")
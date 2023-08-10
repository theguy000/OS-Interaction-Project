import pyautogui
import random
import time
import msvcrt

def keypress():
    return msvcrt.kbhit()

screenWidth, screenHeight = pyautogui.size()

while True:
    if keypress():
        if ord(msvcrt.getch()) == 27: #esc key ASCII
            break

    xMove = random.randint(0, screenWidth)
    yMove = random.randint(0, screenHeight)

    pyautogui.moveTo(xMove, yMove, duration=1)
    time.sleep(random.randint(1,5))
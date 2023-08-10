import random
import time
import msvcrt
def install_package(package):
    try:
        import package
    except ImportError:
        import subprocess
        subprocess.check_call(["python", "-m", "pip", "install", package])

install_package('pyautogui')
import pyautogui

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
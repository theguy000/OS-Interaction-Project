import random
import time
from pynput import keyboard

def install_package(package):
    try:
        import package
    except ImportError:
        import subprocess
        subprocess.check_call(["python", "-m", "pip", "install", package])

install_package('pyautogui')
import pyautogui

# Get screen width and height
screenWidth, screenHeight = pyautogui.size()

# Setting the flag
exit_program = False

def on_press(key):
    global exit_program
    if key == keyboard.Key.esc:
        # if ESC key set flag to True to exit the program
        exit_program = True

# Using a listener to monitor keyboard
listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    if exit_program:
        break

    xMove = random.randint(0, screenWidth)
    yMove = random.randint(0, screenHeight)

    pyautogui.moveTo(xMove, yMove, duration=1)

    time.sleep(random.randint(1,5))
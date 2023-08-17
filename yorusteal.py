import pyautogui
import keyboard

def click():
    for i in range(100):
        pyautogui.click(1200, 1000)

keyboard.add_hotkey("ctrl + shift + z", click())

keyboard.wait('esc')
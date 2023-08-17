import time
import pyautogui

rechargeTime = 20

while True:
    time.sleep(rechargeTime)
    pyautogui.press("7")
    pyautogui.rightClick()
    pyautogui.press("8")
    pyautogui.rightClick()
    pyautogui.press("9")
    pyautogui.rightClick()
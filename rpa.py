import webbrowser
import pyautogui
import pyperclip
import time

url = "https://www.google.com"

webbrowser.open(url, new=0, autoraise=True)

pyautogui.moveTo(470, 340, 1)

pyautogui.click()

pyperclip.copy("平泉町　観光")
pyautogui.hotkey("command", "v")
pyautogui.press('enter')
time.sleep(3)
pyautogui.screenshot('screenshot_hiraizumi.png')

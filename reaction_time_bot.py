import pyautogui
from pyautogui import position, leftClick
import mouse

while True:
    if pyautogui.pixel(425, 465) == (75, 219, 106):
        mouse.click(button=leftClick(425, 465))

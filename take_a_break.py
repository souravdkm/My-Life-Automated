__author__ = 'Om Computers'

import webbrowser
import ctypes  # An included library with Python install.
import time


totalBreaks = 3
breakCount = 0


def openBrowser():
    webbrowser.open("https://www.youtube.com/watch?v=bhgjYM5ZfQA")

def alertNotify():
    ctypes.windll.user32.MessageBoxA(0, "water tip: your body is 70 percent water", "Drink water alert", 0)


while(breakCount < totalBreaks):
    time.sleep(5)
    if(breakCount%2 == 0):
        alertNotify()
    else:
        openBrowser()
        alertNotify()
    breakCount += 1
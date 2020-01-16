import time

from pynput.mouse import Button, Controller


def openFirefoxIncognito():
    mouse = Controller()
    time.sleep(.2)
    mouse.position = (472, 1056)  # moves mouse to Firefox taskbar icon
    mouse.click(Button.right, 1)
    mouse.move(0, -150)
    time.sleep(.4)
    mouse.click(Button.left, 1)


def clickSearchBar():
    mouse = Controller()
    time.sleep(2.9)
    mouse.position = (1009, 90)  # moves to search bar
    mouse.click(Button.left, 9)


def printMouseLocation():
    mouse = Controller()
    time.sleep(2)
    print(mouse.position)


def clickPewdiepieVideo():
    mouse = Controller()
    time.sleep(1.5)
    mouse.position = (529, 500)
    mouse.click(Button.left, 1)


class Mouse:
    def __init__(self):
        pass

import time

from pynput.keyboard import Key, Controller


# types youtube into the url bar
def typeYoutube():
    keyboard = Controller()
    time.sleep(1.3)
    youtube = "Youtube.com"
    for char in youtube:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.03)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


# types into searchbar into the search bar
def typeIntoSearchBar(searchRequest):
    keyboard = Controller()
    time.sleep(2)
    search = searchRequest
    for char in search:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.03)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def hitFForFullScreen():
    keyboard = Controller()
    time.sleep(2.5)
    keyboard.press('f')
    keyboard.release('f')


class Keyboard:
    def __init__(self):
        pass

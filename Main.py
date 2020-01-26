import speech_recognition as sr

import KeyboardControl as Keyboard
import MouseControl as Mouse


def readVoice():
    r = sr.Recognizer()
    #r.energy_threshold = 300 #changes the level of how loud I need to be. Default is 300
    mic = sr.Microphone()
    with mic as source:
        print('What channel do you want to watch?\n')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            print("Nothing")


searchRequest = readVoice()
print(searchRequest)
Mouse.openFirefoxIncognito()
Keyboard.typeYoutube()
Mouse.clickSearchBar()
Keyboard.typeIntoSearchBar(searchRequest)
Mouse.clickPewdiepieVideo()
Keyboard.hitFForFullScreen()

import speech_recognition as sr

import KeyboardControl as Keyboard
import MouseControl as Mouse


def readVoice():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print('What channel do you want to watch?\n')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            # print('You said: {}
            return text
        except:
            print("Nothing")


channelToWatch = readVoice()
print(channelToWatch)
Mouse.openFirefoxIncognito()
Keyboard.typeYoutube()
Mouse.clickSearchBar()
Keyboard.typePewds(channelToWatch)
Mouse.clickPewdiepieVideo()
Keyboard.hitFForFullScreen()

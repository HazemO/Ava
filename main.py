# NOTE: this example requires PyAudio because it uses the Microphone class

#import libs

import speech_recognition as sr
import pyaudio
import os

r = sr.Recognizer()

#identifiy the default microphone
with sr.Microphone() as source:
    #listen to a command, AVD

    while True:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)   
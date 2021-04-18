import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()


def eithne_talk(audio_string):
    talk = gTTS(text=audio_string, lang='en')
    ran = random.randint(1, 100000)
    audio_file = 'audio-' + str(ran) + '.mp3'
    talk.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def record_audio(ask=''):
    # Create a microphone instance.
    with sr.Microphone() as source:
        if ask:
            eithne_talk(ask)
        # Listen for input.
        audio = r.listen(source)
        user_input = ''
        try:
            user_input = r.recognize_google(audio)
        except sr.UnknownValueError:
            eithne_talk('Sorry I did not get that')
        except sr.RequestError:
            eithne_talk('Sorry, my speech service is down')
        return user_input


def respond(user_input):
    if 'what time is it' in user_input:
        eithne_talk('The time is ' + ctime())
    if 'search' in user_input:
        search = record_audio('What would you like to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        eithne_talk('Here is what I found for ' + search)
    if 'find location' in user_input:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        eithne_talk('Here is the location of ' + location)
    if 'turn off' in user_input:
        eithne_talk('Goodbye')
        exit()


def eithne():
    eithne_talk('Hello, my name is Eithne. How can I help?')
    time.sleep(1)
    while 1:
        user_input = record_audio()
        respond(user_input)


if __name__ == "__main__":
    eithne()

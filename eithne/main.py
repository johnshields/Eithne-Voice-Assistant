"""
John Shields - G00348436
Main Controller of Eithne.

References:
https://youtu.be/x8xjj6cR9Nc
https://towardsdatascience.com/how-to-build-your-own-ai-personal-assistant-using-python-f57247b4494b
"""
import datetime
import os
import random
import time
import webbrowser as wb

import playsound
import speech_recognition as sr
import wikipedia
from gtts import gTTS

from user_phrases import user_said

r = sr.Recognizer()


def eithne_talk(audio_string):
    talk = gTTS(text=audio_string, lang='en')
    ran_num = random.randint(1, 100000)
    audio_file = 'audio-' + str(ran_num) + '.mp3'
    talk.save(audio_file)
    playsound.playsound(audio_file)
    print('Eithne said:', audio_string)
    os.remove(audio_file)


def user_audio(ask=''):
    # Create a microphone instance.
    with sr.Microphone() as source:
        if ask:
            eithne_talk(ask)
        # Listen for input.
        audio = r.listen(source)
        user_input = ''
        try:
            user_input = r.recognize_google(audio, language='en')
        except sr.UnknownValueError:
            eithne_talk('Did you say something?')
            user_input = ''
        except sr.RequestError:
            eithne_talk('Sorry, my respond service is down')
            exit()
        print('$', user_input.lower())
        return user_input.lower()


def respond(user_input):
    if 'name' == user_said(user_input):
        name = user_audio('My name is Eithne. What is yours?')
        eithne_talk('Hi ' + name)
    # Allow user to thank Eithne.
    if 'thank' == user_said(user_input):
        eithne_talk('No bother')
        user_input = ''
    # Tell user the time.
    if 'time' == user_said(user_input):
        t = datetime.datetime.now().strftime("%H:%M:%S")
        eithne_talk('The time is ' + str(t) + '12')
        user_input = ''
    # Let user do a google search.
    if 'search' == user_said(user_input):
        search = user_audio('What would you like to search for?')
        url = 'https://google.com/search?q=' + search
        wb.get().open(url)
        eithne_talk('Here is what I found for ' + search)
        user_input = ''
    # Let user find a location.
    if 'location' == user_said(user_input):
        location = user_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        wb.get().open(url)
        eithne_talk('Here is the location of ' + location)
        user_input = ''
    if 'wikipedia' == user_said(user_input):
        wiki = user_audio('What would you like to know more about?')
        results = wikipedia.summary(wiki, sentences=3)
        eithne_talk('According to wikipedia ' + results)
    # Allow user to stop Eithne.
    if 'stop' == user_said(user_input):
        eithne_talk('farewell')
        exit()


# Greet the user.
def greeting():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        eithne_talk("Hello, Good Morning")
    elif 12 <= hour < 18:
        eithne_talk("Hello, Good Afternoon")
    else:
        eithne_talk("Hello, Good Evening")


def eithne():
    print('====== Eithne, Voice Assistant ======')
    greeting()
    eithne_talk('How can I help?')
    time.sleep(1)
    while 1:
        user_input = user_audio()
        respond(user_input)


if __name__ == "__main__":
    eithne()

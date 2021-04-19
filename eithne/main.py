"""
John Shields - G00348436
Main Controller of Eithne.

Reference: https://youtu.be/x8xjj6cR9Nc
"""


import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime
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
            print('No voice input heard')
        except sr.RequestError:
            eithne_talk('Sorry, my speech service is down')
            exit()
        print('$', user_input.lower())
        return user_input.lower()


def get_time():
    t = ctime().split(' ')[3].split(':')[0:2]
    if t[0] == '00':
        hours = '12'
    else:
        hours = t[0]
    minutes = t[1]
    t = hours + ' hours and ' + minutes + ' minutes'
    return t


def respond(user_input):
    # Tell user the time.
    if 'time' in user_said(user_input):
        eithne_talk('The time is ' + str(get_time()))
    # Let user do a google search.
    if 'search' in user_said(user_input):
        search = record_audio('What would you like to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        eithne_talk('Here is what I found for ' + search)
    # Let user find a location.
    if 'location' in user_said(user_input):
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        eithne_talk('Here is the location of ' + location)
    # Allow user to stop Eithne.
    if 'stop' in user_said(user_input):
        eithne_talk('farewell')
        exit()


def eithne():
    print('====== Eithne, Voice Assistant ======')
    eithne_talk('Hello, my name is Eithne. How can I help?')
    time.sleep(1)
    while 1:
        user_input = record_audio()
        respond(user_input)


if __name__ == "__main__":
    eithne()

"""
John Shields - G00348436
Main Controller of Eithne.

References:
https://youtu.be/x8xjj6cR9Nc
https://bit.ly/3auyANP
https://realpython.com/python-speech-recognition/
"""
import datetime as dt
import logging
import os
import random
import time

import playsound
import speech_recognition as sr
import wikipedia
from gtts import gTTS

from features import google, maps, on_this_day, youtube, websites
from user_phrases import user_said

# Load in recognizer.
r = sr.Recognizer()

# Debugging
logging.basicConfig(level=logging.INFO)


# Function to use google text to speech for Eithne's voice.
def eithne_talk(audio_string):
    # Set up Eithne's vocals.
    talk = gTTS(text=audio_string, lang='en')
    ran_num = random.randint(1, 100000)
    # Set to random mp3 file and save.
    audio_file = 'audio-' + str(ran_num) + '.mp3'
    talk.save(audio_file)
    # Play what Eithne said then remove the mp3.
    playsound.playsound(audio_file)
    print('Eithne said:', audio_string)
    os.remove(audio_file)


# Set up the microphone for the user.
def user_audio(ask=''):
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    # Create a microphone instance.
    with sr.Microphone() as source:
        if ask:
            eithne_talk(ask)
        # Listen for input.
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=5.0)
        user_input = ''

        if not isinstance(r, sr.Recognizer):
            raise TypeError('`recognizer` must be `Recognizer` instance')

        if not isinstance(source, sr.Microphone):
            raise TypeError('`microphone` must be a `Microphone` instance')

        try:
            user_input = r.recognize_google(audio, language='en')
        except sr.UnknownValueError:
            # speech was unintelligible
            print('No voice input heard')
        except sr.RequestError:
            # API was unreachable or unresponsive
            eithne_talk('Sorry, my response service is down')
            exit()
        print('$', user_input.lower())
        return user_input.lower()


# Eithne responds to the user bases on their request.
def respond(user_input):
    # Allow user to ask for VA's name then say 'Hi' with the user's said name.
    if 'name' in user_said(user_input):
        name = user_audio('My name is Eithne. What is yours?')
        eithne_talk('Hi ' + name)
    # Allow user to thank Eithne.
    if 'thank' in user_said(user_input):
        good_bye = ['No bother', 'No problem', "You're welcome", "Don't mention it"]
        message = good_bye[random.randint(0, len(good_bye) - 1)]
        eithne_talk(message)
    # Let user do a google search.
    if 'search' in user_said(user_input):
        search = user_audio('What would you like to search for?')
        google(search)
        eithne_talk('Here is what I found for ' + search + ' on google')
    # Let user find a location.
    if 'location' in user_said(user_input):
        location = user_audio('What is the location?')
        maps(location)
        eithne_talk('Here is the location of ' + location)
    # Allow user to use wiki.
    if 'wikipedia' in user_said(user_input):
        wiki = user_audio('What would you like to know more about?')
        results = wikipedia.summary(wiki, sentences=3)
        eithne_talk('According to wikipedia ' + results)
    # Tell the User what happened on this day.
    if 'history' == user_said(user_input):
        eithne_talk('Today ' + on_this_day())
    # Allow user to find a video on YouTube.
    if 'youtube' in user_said(user_input):
        search = user_audio('What video would you like to watch?')
        youtube(search)
        eithne_talk('Here is what I found for ' + search + ' on youtube')
    # Allow user to surf the web.
    if 'web' in user_said(user_input):
        surf = user_audio('Which website would you like to surf?')
        websites(surf)
        eithne_talk(surf + ' opened')
    # Allow user to stop Eithne.
    if 'stop' in user_said(user_input):
        good_bye = ['Farewell', 'Goodbye', 'Good luck', 'See ya', 'So long']
        message = good_bye[random.randint(0, len(good_bye) - 1)]
        eithne_talk(message)
        exit()


# Greet the user.
def greeting():
    hour = dt.datetime.now().hour
    if 0 <= hour < 12:
        eithne_talk('Good Morning')
    elif 12 <= hour < 18:
        eithne_talk('Good Afternoon')
    else:
        eithne_talk('Good Evening')


# Main function to boot up Eithne and greet the user.
def eithne():
    print('====== Eithne, Voice Assistant ======')
    greeting()
    help_ful = ['How can I help?', 'What would you like to do today?',
                'What service do you require?', "I'm listening"]
    message = help_ful[random.randint(0, len(help_ful) - 1)]
    eithne_talk(message)
    time.sleep(1)
    while 1:
        user_input = user_audio()
        respond(user_input)


if __name__ == "__main__":
    eithne()

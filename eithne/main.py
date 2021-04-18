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
    ran_num = random.randint(1, 100000)
    audio_file = 'audio-' + str(ran_num) + '.mp3'
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
        print('No voice input heard')
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
        t = ctime().split(' ')[3].split(':')[0:2]
        if t[0] == '00':
            hours = '12'
        else:
            hours = t[0]
        minutes = t[1]
        t = hours + ' hours and ' + minutes + ' minutes'
        eithne_talk('the time is ' + str(t))
    if 'search' in user_input:
        search = record_audio('what would you like to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        eithne_talk('here is what I found for ' + search)
    if 'find location' in user_input:
        location = record_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        eithne_talk('here is the location of ' + location)
    if 'turn off' in user_input:
        eithne_talk('Goodbye')
        exit()


def eithne():
    eithne_talk('Hello, my name is Eithne. How can I help?')
    time.sleep(1)
    while 1:
        user_input = record_audio()
        print(user_input)
        respond(user_input)


if __name__ == "__main__":
    eithne()

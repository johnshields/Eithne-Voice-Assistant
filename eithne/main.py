"""
@author John Shields - G00348436
Main Controller of Eithne.

References:
https://youtu.be/x8xjj6cR9Nc
https://bit.ly/3auyANP
https://realpython.com/python-speech-recognition/
https://chatterbot.readthedocs.io/en/stable/training.html
"""
import datetime as dt
import os
import random
import time

import playsound
import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from gtts import gTTS

from features import *
from user_phrases import user_said

# Load in recognizer.
r = sr.Recognizer()

# Set up Eithne as a chat bot.
eithne_bot = ChatBot('Eithne Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
                     logic_adapters=['chatterbot.logic.BestMatch'], database_uri='sqlite:///database.db')

# Train the bot.
trainer = ListTrainer(eithne_bot)
"""
Training the chat bot with different commands a user could say with responses for Eithne to say.
#1:= User Command #2:= Bot Response
"""
# Responses for an introduction...
trainer.train(["what is your name", "My name is Eithne. What is yours?"])
trainer.train(["who are you", "I'm Eithne. Who are you?"])
trainer.train(["hi", "Hi my name is Eithne. What is yours?"])
trainer.train(["hello", "Hello, I'm Eithne. You?"])
trainer.train(["hey", "Hey yourself! Eithne here. What's your name?"])
# Responses for thanking Eithne.
trainer.train(["thank you", "You're welcome!"])
trainer.train(["thanks", "Don't mention it!"])
trainer.train(["sound", "No bother!"])
trainer.train(["cheers", "No problem!"])
# Responses to google search cmds.
trainer.train(["search", "What would you like to search for?"])
trainer.train(["do a search", "Google is loaded for searching!"])
trainer.train(["google", "Google is waiting for your request!"])
trainer.train(["google search", "Search away!"])
trainer.train(["open google", "Google is waiting your command!"])
# Responses to location cmds.
trainer.train(["location", "What is the location?"])
trainer.train(["maps", "What place?"])
trainer.train(["find location", "Where is your next adventure?"])
trainer.train(["where can i find", "Find what?"])
trainer.train(["open maps", "Maps is at your command!"])
# Responses to wikipedia cmds.
trainer.train(["wikipedia", "What would you like to know more about?"])
trainer.train(["wiki", "Hmm, what topic?"])
# Responses to youtube cmds.
trainer.train(["youtube", "YouTube is waiting for a query!"])
trainer.train(["video", "What video?"])
trainer.train(["i would like to watch a video", "Which one?"])
trainer.train(["open youtube", "YouTube is at your command!"])
# Responses for website request.
trainer.train(["website", "Which website?"])
trainer.train(["surf the web", "Which website would you like to surf?"])
trainer.train(["internet", "What would you like to see?"])
trainer.train(["online", "Online. Waiting on your command!"])
# Responses for when Eithne is requested to turn off.
trainer.train(["turn off", "Farewell"])
trainer.train(["stop listening", "Goodbye"])
trainer.train(["exit", "Good Luck"])
trainer.train(["quit", "So long"])


# Function to take in a user command and return a response from the bot.
def bot_response(cmd):
    response = eithne_bot.get_response(cmd)
    return str(response)


# Function to use Google text-to-speech for Eithne's voice.
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


# User interaction controller
# Sets up the microphone for the user.
# Listen for user input, if there is an input return it.
def user_audio(ask=''):
    # Create a microphone instance.
    with sr.Microphone() as source:
        # If the command requires 2 inputs from the user.
        if ask:
            eithne_talk(ask)

        # Listen for user input.
        audio = r.listen(source)
        user_input = ''

        try:
            # Try to listen for user input...
            user_input = r.recognize_google(audio, language='en')
        except sr.UnknownValueError:
            # If nothing was said or speech was 'unintelligible'.
            print('No voice input recognized')
        except sr.RequestError:
            # Speech Recognition is unreachable or unresponsive.
            eithne_talk('Sorry, it appears that the speech recognition service is down.')
            exit()
        print('$', user_input.lower())
        return user_input.lower()  # Return the user's input.


# Response controller
# Allows user and Eithne to talk back and forth.
# Works with user_phrases.py, features.py, eithne_talk, bot_response and user_audio.
# Eithne responds to the user based on their request.
def respond(user_input):
    # Allow user to ask for VA's name then say 'Hi' with the user's said name.
    if 'name' in user_said(user_input):
        name = user_audio(bot_response(user_input))  # Get response from trained bot.
        eithne_talk(f'Hi {name}')
    # Allow user to find out more about Eithne.
    elif 'about' in user_said(user_input):
        eithne_talk(about())
    # Allow user to thank Eithne.
    elif 'thank' in user_said(user_input):
        eithne_talk(bot_response(user_input))
    # Let user do a google search.
    elif 'search' in user_said(user_input):
        search = user_audio(bot_response(user_input))
        google(search)
        eithne_talk(f'Here is what I found for {search} on Google')
    # Let user find a location.
    elif 'location' in user_said(user_input):
        location = user_audio(bot_response(user_input))
        maps(location)
        eithne_talk(f'Here is the location of {location}')
    # Allow user to use wikipedia.
    elif 'wikipedia' in user_said(user_input):
        wiki_sum = user_audio(bot_response(user_input))
        eithne_talk(f'According to wikipedia {wiki(wiki_sum)}')
    # Tell the User what happened on this day in history.
    elif 'history' == user_said(user_input):
        eithne_talk(f'Today {on_this_day()}')
    # Allow user to find a video on YouTube.
    elif 'youtube' in user_said(user_input):
        query = user_audio(bot_response(user_input))
        youtube(query)
        eithne_talk(f'Here are videos for {query} on YouTube')
    # Allow user to surf the web.
    elif 'web' in user_said(user_input):
        surf = user_audio(bot_response(user_input))
        websites(surf)
        eithne_talk(f'{surf} opened')
    # Allow user to stop Eithne.
    elif 'stop' in user_said(user_input):
        eithne_talk(bot_response(user_input))
        exit()
    else:
        n = ['Sorry I cannot process that command', 'Did you say something?',
             'Are you alright?', 'Unreachable command', "Sorry, what was that?", "Does not compute"]
        message = n[random.randint(0, len(n) - 1)]
        eithne_talk(message)


# Greet the user depending what time of the day it is.
def greeting():
    hour = dt.datetime.now().hour
    if 0 <= hour < 12:
        eithne_talk('Good Morning')
    elif 12 <= hour < 18:
        eithne_talk('Good Afternoon')
    else:
        eithne_talk('Good Evening')


# Main function to boot up Eithne and greet the user.
# Then start a loop to listen in for user input and have Eithne to respond back.
def eithne():
    print('====== Eithne, Voice Assistant ======')
    greeting()
    help_ful = ['How can I help?', 'What would you like to do today?', 'What service do you require?',
                "I'm listening", "What can I do for you?", "Thanks for waking me up!"]
    message = help_ful[random.randint(0, len(help_ful) - 1)]
    eithne_talk(message)
    time.sleep(1)
    # Start up interaction.
    while 1:
        user_input = user_audio()
        respond(user_input)


if __name__ == "__main__":
    eithne()

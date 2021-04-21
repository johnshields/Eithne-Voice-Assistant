"""
John Shields - G00348436
Features Controller
Eithne's features for google, maps, history, youtube and websites.
"""
import logging
import webbrowser as wb
from datetime import datetime

import requests as req
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Debugging
from main import eithne_talk, user_audio

logging.basicConfig(level=logging.INFO)

# Set up Eithne as a chat bot.
eithne_bot = ChatBot(
    'Eithne Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)


def train_bot():
    # Train the bot.
    trainer = ChatterBotCorpusTrainer(eithne_bot)
    trainer.train("chatterbot.corpus.english")


def google(search):
    url = f'https://google.com/search?q={search}'
    wb.get().open(url)


def maps(location):
    url = f'https://google.nl/maps/place/{location}/&amp;'
    wb.get().open(url)


def on_this_day():
    d = datetime.today().strftime('%d')
    m = datetime.today().strftime('%m')
    url = f'http://numbersapi.com/{m}/{d}/date'
    resp = req.get(url)
    return resp.text


def youtube(video):
    url = f'https://www.youtube.com/results?search_query={video}'
    wb.get().open(url)


def websites(website):
    url = f'https://www.{website}.com'
    wb.get().open(url)


# TODO: FIX!! - Every answer is just this!!
# Have a chat with Eithne.
def conversation(topic):
    print('having a chat...')
    response = eithne_bot.get_response(user_audio(topic))
    eithne_talk(str(response))

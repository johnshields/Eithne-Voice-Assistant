"""
John Shields - G00348436
Testing Bot from ChatterBot
Mainly to acquire accurate responses.
https://chatterbot.readthedocs.io/en/stable/training.html
"""

import logging

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

logging.basicConfig(level=logging.INFO)

# Set up Eithne as a chat bot.
eithne_bot = ChatBot('Eithne Bot',
                     storage_adapter='chatterbot.storage.SQLStorageAdapter',
                     logic_adapters=['chatterbot.logic.BestMatch'],
                     database_uri='sqlite:///database.db'
                     )

# Train the bot.
trainer = ListTrainer(eithne_bot)
# User wants Eithne to stop listening.
# 1: = User cmd  # 2: = response
trainer.train(["turn off", "Farewell"])
trainer.train(["stop listening", "Goodbye"])
trainer.train(["exit", "Good Luck"])
trainer.train(["quit", "So long"])
# User wants do a google search.
trainer.train(["search", "What would you like to search for?"])
trainer.train(["do a search", "Google is loaded for searching"])
trainer.train(["google", "Google is waiting for your request"])
trainer.train(["google search", "search away"])
trainer.train(["open google", "Google is at your service"])
# User wants to find a location.
trainer.train(["location", "What is the location?"])
trainer.train(["maps", "What place?"])
trainer.train(["find location", "where is your next adventure?"])
trainer.train(["where can i find", "Find what?"])
trainer.train(["open maps", "maps is at your service"])
# User wants to use wiki.
trainer.train(["wikipedia", "What would you like to know more about?"])
trainer.train(["wiki", "Hmm, what topic?"])
# User wants to search youtube.
trainer.train(["youtube", "YouTube is waiting for a query"])
trainer.train(["video", "What video?"])
trainer.train(["i would like to watch a video", "Which one?"])
trainer.train(["open youtube", "Youtube is at your service"])
# Responses for website request.
trainer.train(["website", "which website?"])
trainer.train(["surf the web", "Which website would you like to surf?"])
trainer.train(["internet", "What would you like to see?"])
trainer.train(["online", "Online. Waiting on your command"])
# Responses for thanking Eithne.
trainer.train(["thank you", "You're welcome"])
trainer.train(["thanks", "Don't mention it"])
trainer.train(["sound", "No bother"])
trainer.train(["cheers", "No problem"])
# Responses for when Eithne shuts down.
trainer.train(["turn off", "Farewell"])
trainer.train(["stop listening", "Goodbye"])
trainer.train(["exit", "Good Luck"])
trainer.train(["quit", "So long"])

print('talk to bot')
while True:
    phrase = input()
    response = eithne_bot.get_response(phrase)
    print(f'bot: {response}')

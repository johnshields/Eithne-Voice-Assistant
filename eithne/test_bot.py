"""
John Shields - G00348436
Testing Bot from ChatterBot
Mainly to acquire accurate responses.
"""

import logging

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

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

# Train the bot.
trainer = ListTrainer(eithne_bot)
trainer.train([
    "hi there",
    "Hello",
])

phrase = input()
response = eithne_bot.get_response(phrase)
print(response)

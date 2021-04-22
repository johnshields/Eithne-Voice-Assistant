<h1 align="center">Gesture Based UI Development</h1>


<a href="https://www.gmit.ie/">
<p align="center"><img src="https://i.ibb.co/f1ZQSkt/logo-gmit.png"
alt="GMIT Logo" width="500" height="200"/>
</p></a>


<H3 align="center">John Shields - G00348436</H3>

***

<a href="https://github.com/johnshields/Eithne-Voice-Assistant">
<p align="center"><img src="https://bit.ly/3eqTQ8r" alt="eithne_logo" width="200"/></p>
</a>

* GitHub Repository URL: https://github.com/johnshields/Eithne-Voice-Assistant

# Overview

Originally for this project, a Virtual Reality detective game was the first choice. This game would have been developed
with Unity and the Oculus Quest. Unfortunately, due to PC hardware limitations, it was not feasible to develop a
sufficient game. Many attempts were made to get the game set up, but even basic setups took hours. Being a hectic time
during the college year, this could not carry on. Time is precious; therefore, improvisation had to be made. The
project's goal was then altered to be a Voice Assistant in Python with skills enhanced by AI technologies.

# Purpose of the Application
The application designed is a Voice Assistant by the name of Eithne. Eithne takes in a voice command from a user and
responds to the user depending on the commands (Figure Below). The user's voice input is done by
a [Speech Recognition](https://pypi.org/project/SpeechRecognition/) import and Eithne's voice comes from
the [Google Text-To-Speech](https://pypi.org/project/gTTS/) import.

### User Input and Response System

![user-to-eithne](https://user-images.githubusercontent.com/26766163/115746073-ed2f1700-a38b-11eb-8d34-0e51c860d5d3.png)

## Features

Eithne is programmed to do the following features:

* Google Search
* Google Maps
* Wikipedia Summaries
* YouTube Queries
* Open any Website with a ``dot com``
* Historical Events that happened Today from [numbersapi.com/day/month/date](http://numbersapi.com/04/6/date)

See the figures below for demonstrations of how the user interacts with Eithne's integrated features.

### Google Search Feature

![google_search](https://user-images.githubusercontent.com/26766163/115704335-27d08980-a363-11eb-9e0b-bd45794fcc7e.png)

### Google Maps Feature

![maps](https://user-images.githubusercontent.com/26766163/115704402-3dde4a00-a363-11eb-8b2c-09354da9b27d.png)

### Wikipedia Summaries Feature

![wiki](https://user-images.githubusercontent.com/26766163/115704633-8433a900-a363-11eb-8720-e4b4a0f741cc.png)

### YouTube Queries Feature

![youtube](https://user-images.githubusercontent.com/26766163/115704566-6d8d5200-a363-11eb-83bd-2949ff73d88e.png)

### Website Feature - Twitter

![twitter](https://user-images.githubusercontent.com/26766163/115704445-4b93cf80-a363-11eb-80d2-7639cff6c701.png)

### Historical Events Feature

![history](https://user-images.githubusercontent.com/26766163/115704375-34ed7880-a363-11eb-884b-d75f6cc6e5fb.png)

# Gestures of this application

***Consider how gestures can be incorporated into the application, providing a justification for the ones that you pick.
This is an important research element for the project and needs to explain how the gestures fit into the solution you
are creating.***

The application is entirely controlled by voice. Meaning the gestures implemented are user commands and also what
Eithne says back to the user. The user controls Eithne by having almost a conversation for each command as they always
get a response no matter what the user says. Being a voice assistant, the commands had to be pretty open so that they would
come naturally to the user. In order to achieve this in `user_phrases.py` a function was created to return many possible
commands a user could say for the features above. Also, there are simple commands for example `Hi`, `Hello`, `Hey` all return
with a response by Eithne asking for the user's name. 
For Eithne's responses, a machine learning (ML) mechanism was used to get different responses for each command. The following
are the programmed commands, but the user is not limited to just these as the ML mechanism can understand similar
commands to the ones said and still give back a response. The ML mechanism will be discussed in far more detail
in ***Architecture for the solution***. 

For the features Google Search, Google Maps, Wikipedia, YouTube Queries and Website the user is required to say two commands.
On for activating the feature and one for controlling what they want the feature to do. 
There are figures under the commands for these features for further explanation.

| User wants to know the VA's name or wants to say hello.|  |
| :-------------      |:-------------|
| **User Input**      | **Response** |
| What is your name?  | My name is Eithne. What is yours? |
| Who are you?        | I'm Eithne. Who are you? |
| Hi                  | Hi my name is Eithne. What is yours? |
| Hello               | Hello, I'm Eithne. You? |
| Hey                 | Hey yourself! Eithne here. What's your name? |

After the User says their name Eithne will say Hi with the user's name (Figure below).

![hi](https://user-images.githubusercontent.com/26766163/115764058-02607180-a39d-11eb-8989-3e00a598ee64.png)

| User wants to know what Eithne can do. |  |
| :-------------      |:-------------|
| **User Input**      | **Response** |
| Tell me about yourself  | I am a voice assistant named Eithne... |
| Talk about yourself     |                 ^^                     |
| What can you do?        |                 ^^                     |
| About                   |                 ^^                     |

| User wants to thank Eithne.|       |
| :-------------      |:-------------|
| **User Input**      | **Response** |
| Thank you  | You're welcome! |
| Thanks     | Don't mention it! |
| Sound      | No bother! |
| Cheers     | No problem! |

|  User wants do a Google Search.      | |
| :-------------      |:-------------|
| **User Input**      | **Response** |
| Search       | What would you like to search for? |
| Do a Search  | Google is loaded for searching! |
| Google search | Search away! |
| Open google | Google is waiting your command! |

![search](https://user-images.githubusercontent.com/26766163/115765992-52d8ce80-a39f-11eb-834c-15baaf06ec91.png)

|  User wants to find a location.      | |
| :-------------      |:-------------|
| **User Input**      | **Response** |
| Location         | What is the location? |
| Maps             | What place? |
| Find location    | Where is your next adventure? |
| Where can I find | Find what? |
| Open Maps        | Maps is at your command! |

![location](https://user-images.githubusercontent.com/26766163/115767277-db0ba380-a3a0-11eb-982c-08834011c093.png)

|  User wants to use Wikipedia. | |
| :-------------      |:-------------|
| **User Input**      | **Response** |
| Wikipedia | What would you like to know more about? |
| Wiki      | Hmm, what topic? |

![gbh](https://user-images.githubusercontent.com/26766163/115769907-ffb54a80-a3a3-11eb-8d35-888c5f8a5758.png)

|  User wants to know what happened today.     | |
| :-------------      |:-------------|
| **User Input**      | **Response** |
| History                               | Historical events that happened today... |
| What happened today?                  |              ^^                 |
| History of today                      |              ^^                 |
| Historical event                      |              ^^                 |

|  User wants to watch a video on YouTube.      | |
| :-------------      |:-------------|
| **User Input**      | **Response** |
| YouTube                          | YouTube is waiting for a query! |
| Video                            | What video? |
| I would like to watch a Video    | Which one? |
| Open YouTube                     | YouTube is at your command! |

![yt](https://user-images.githubusercontent.com/26766163/115770540-c0d3c480-a3a4-11eb-934b-376f21442eb0.png)

|  User wants to surf a website.      | |
| :-------------      |:-------------|
| **User Input**      | **Response** |
| Website          | Which website? |
| Surf the web     | Which website would you like to surf? |
| Internet         | What would you like to see? |
| Online           | Online. Waiting on your command! |

![web](https://user-images.githubusercontent.com/26766163/115772504-1ad58980-a3a7-11eb-80e6-3453264aec5d.png)

| User wants Eithne to stop listening/turn off. | |
| :-------------      |:-------------|
| **User Input**      | **Response** |
| Turn off          | Farewell |
| Stop listening    | Goodbye |
| exit              | Good Luck |
| quit              | So long |

# Hardware used in creating the application

***You are not limited to the hardware listed above. If you have your own hardware, or hardware simulator that you wish
to use, then feel free. The purpose of each piece of hardware should be given with a comparison to other options
available.***

# Architecture for the solution

***The full architecture for the solution, including the class diagrams, any data models, communications and distributed
elements that you are creating. The architecture must make sense when the gestures, and the hardware are combined.
Justification is necessary in the documentation for this. You need to include a list of relevant libraries that you used
in the project.***

## ChatterBot

The majority of Eithne's responses are decided by a machine learning engine
called [ChatterBot](https://chatterbot.readthedocs.io/en/stable/index.html). ChatterBot is used to train Eithne to
respond to user commands for features in the application. The bot is designed to respond to multiple commands for each
feature. The Logic Adapter used for this functionality is `BestMatch`
The code below shows how the bot is trained with possible user commands and set responses.

```python
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Set up Eithne as a chat bot.
eithne_bot = ChatBot('Eithne Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
                     logic_adapters=['chatterbot.logic.BestMatch'], database_uri=None)
# Train the bot.
trainer = ListTrainer(eithne_bot)
# Response to a google search cmd.
trainer.train(["search", "What would you like to search for?"])
trainer.train(["do a search", "Google is loaded for searching!"])
trainer.train(["google", "Google is waiting for your request!"])
trainer.train(["google search", "Search away!"])
trainer.train(["open google", "Google is waiting your command!"])
```

ChatterBot was initially tested with these commands and responds through a command line interaction. This was mainly to
test how the bot learns with each command passed in. The figure below is a command line interaction with the bot that
shows a log output of how it learns as commands are given to it.

### Testing Bot's responses

![bot](https://user-images.githubusercontent.com/26766163/115777593-67bc5e80-a3ad-11eb-859c-c8c4a2b92a55.png)

The voiced responses are handled by the function ``bot_response``

```python
# Function to take in a user command and return a response from the bot.
def bot_response(cmd):
    response = eithne_bot.get_response(cmd)
    return str(response)
```

# Conclusions & Recommendations

***Conclusions are what you have learned from this project, and the associated research. Recommendations are what you
would do differently if you were to undertake the project again. The Reflective Piece – what I learned and “enjoyed”!
This gives scope for a critical evaluation of the project, and the objective that you tried to achieve.***

# References

* [Build A Python Speech Assistant App](https://youtu.be/x8xjj6cR9Nc)
* [How to build your own AI personal assistant using Python](https://bit.ly/3auyANP)
* [The Ultimate Guide To Speech Recognition With Python](https://realpython.com/python-speech-recognition/)
* [ChatterBot](https://chatterbot.readthedocs.io/en/stable/index.html#)

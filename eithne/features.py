"""
@author John Shields - G00348436
Features Controller
Eithne's features for google, maps, wikipedia, history, youtube and websites.

References:
https://youtu.be/x8xjj6cR9Nc
https://bit.ly/3auyANP
"""
import webbrowser as wb
from datetime import datetime

import requests as req
import wikipedia


# Function to return a description of Eithne.
def about():
    about_eithne = "I am a voice assistant named Eithne. " \
                   "I am programmed to do the following features: " \
                   "Google Search, Google Maps, YouTube Queries, Wikipedia Summaries, " \
                   "open any Website with a dot com and I can tell you Historical Events that happened Today."
    return about_eithne


# Function to take in user input and do a google search.
def google(search):
    # Set up URL.
    url = f'https://google.com/search?q={search}'
    wb.get().open(url)  # Open browser with URL


# Function to take in user input and use google maps.
def maps(location):
    url = f'https://google.nl/maps/place/{location}/&amp;'
    wb.get().open(url)


# Function to take in user input and return a wikipedia summary.
def wiki(wiki_search):
    result = wikipedia.summary(wiki_search, sentences=3)
    return result


# Function to get Historical Events that happened Today.
def on_this_day():
    d = datetime.today().strftime('%d')
    m = datetime.today().strftime('%m')
    # Set up URL.
    url = f'http://numbersapi.com/{m}/{d}/date'
    # Do GET request.
    resp = req.get(url)
    return resp.text  # return the response bodies text


# Function to take in user input for a youtube search.
def youtube(video):
    url = f'https://www.youtube.com/results?search_query={video}'
    wb.get().open(url)


# Function to take in user input to go to a specific website
def websites(website):
    url = f'https://www.{website}.com'
    wb.get().open(url)

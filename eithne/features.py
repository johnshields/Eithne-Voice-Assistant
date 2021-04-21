"""
@author John Shields - G00348436
Features Controller
Eithne's features for google, maps, history, youtube and websites.

Reference: https://bit.ly/3auyANP
"""
import webbrowser as wb
from datetime import datetime

import requests as req


# Function to take in user input and do a google search.
def google(search):
    url = f'https://google.com/search?q={search}'
    wb.get().open(url)


# Function to take in user input and use google maps.
def maps(location):
    url = f'https://google.nl/maps/place/{location}/&amp;'
    wb.get().open(url)


# Function to get a 'history of today'.
def on_this_day():
    d = datetime.today().strftime('%d')
    m = datetime.today().strftime('%m')
    url = f'http://numbersapi.com/{m}/{d}/date'
    resp = req.get(url)
    return resp.text


# Function to take in user input for a youtube search.
def youtube(video):
    url = f'https://www.youtube.com/results?search_query={video}'
    wb.get().open(url)


# Function to take in user input to go to a specific website
def websites(website):
    url = f'https://www.{website}.com'
    wb.get().open(url)

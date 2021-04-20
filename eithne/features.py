"""
John Shields - G00348436
Features Controller
Eithne's features for google, maps, history, youtube and websites.
"""


import webbrowser as wb
from datetime import datetime

import requests as req


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



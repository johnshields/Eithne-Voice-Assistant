"""
@author John Shields - G00348436
User Phrases Controller
To allow users to have an option of what to say for different commands.
"""


def user_said(phrase):
    p = phrase
    # User wants to know what Eithne can do.
    if 'tell me about yourself' in p or 'talk about yourself' in p or 'what can you do' in p or 'about' in p:
        p = 'about'
    # User wants Eithne to stop listening.
    if 'turn off' in p or 'stop listening' in p or 'exit' in p or 'quit' in p:
        p = 'stop'
    # User wants do a google search.
    if 'search' in p or 'do a search' in p or 'google' in p or 'google search' in p or 'open google' in p:
        p = 'search'
    # User wants to find a location.
    if 'location' in p or 'maps' in p or 'find location' in p or 'where can i find' in p or 'open maps' in p:
        p = 'location'
    # User wants to thank Eithne.
    if 'thank you' in p or 'thanks' in p or 'sound' in p or 'cheers' in p:
        p = 'thank'
    # User wants to use wiki.
    if 'wikipedia' in p or 'wiki' in p:
        p = 'wikipedia'
    # User wants to know the VA's name.
    if 'what is your name' in p or 'who are you' in p:
        p = 'name'
    # User whats to know what happened today.
    if 'history' in p or 'what happened today' in p or 'history of today' in p or 'happened today' in p or 'today' in p:
        p = 'history'
    # User wants to search youtube.
    if 'youtube' in p or 'video' in p or 'i would like to watch a video' in p or 'open youtube' in p:
        p = 'youtube'
    # User wants to surf a website.
    if 'website' in p or 'surf the web' in p or 'internet' in p or 'online' in p:
        p = 'web'
    return p

"""
@author John Shields - G00348436
User Phrases Controller
To allow users to have an option of what to say for different commands.
"""


def user_said(phrase):
    p = phrase
    # User wants to know the VA's name.
    if 'what is your name' in p or 'who are you' in p or 'hi' in p or 'hello' in p or 'hey' in p:
        p = 'name'
    # User wants to know what Eithne can do.
    elif 'tell me about yourself' in p or 'talk about yourself' in p or 'what can you do' in p or 'about' in p:
        p = 'about'
        # User wants to thank Eithne.
    elif 'thank you' in p or 'thanks' in p or 'sound' in p or 'cheers' in p:
        p = 'thank'
    # User wants do a google search.
    elif 'search' in p or 'do a search' in p or 'google' in p or 'google search' in p or 'open google' in p:
        p = 'search'
    # User wants to find a location.
    elif 'location' in p or 'maps' in p or 'find location' in p or 'where can i find' in p or 'open maps' in p:
        p = 'location'
    # User wants to use wiki.
    elif 'wikipedia' in p or 'wiki' in p:
        p = 'wikipedia'
    # User whats to know what happened today.
    elif 'history' in p or 'what happened today' in p or 'history of today' in p or 'happened today' in p or 'today' in p:
        p = 'history'
    # User wants to search youtube.
    elif 'youtube' in p or 'video' in p or 'i would like to watch a video' in p or 'open youtube' in p:
        p = 'youtube'
    # User wants to surf a website.
    elif 'website' in p or 'surf the web' in p or 'internet' in p or 'online' in p:
        p = 'web'
    # User wants Eithne to stop listening.
    elif 'turn off' in p or 'stop listening' in p or 'exit' in p or 'quit' in p:
        p = 'stop'
    return p
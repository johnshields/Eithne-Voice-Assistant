def user_said(phrase):
    p = phrase
    # User wants Eithne to stop listening.
    if 'turn off' in p or 'stop listening' in p or 'exit' in p or 'quit' in p:
        phrase = 'stop'
    # User wants do a google search.
    if 'search' in p or 'do a search' in p or 'google' in p or 'google search' in p:
        phrase = 'search'
    # User wants to find a location.
    if 'location' in p or 'maps' in p or 'find location' in p or 'where can i find' in p:
        phrase = 'location'
    # User wants to thank Eithne.
    if 'thank you' in p or 'thanks' in p or 'sound' in p or 'cheers' in p:
        phrase = 'thank'
    # User wants to use wiki.
    if 'wikipedia' in p or 'wiki' in p:
        phrase = 'wikipedia'
    # User wants to know the VA's name.
    if 'what is your name' in p or 'who are you' in p:
        phrase = 'name'
    # User whats to know what happened today.
    if 'history' in p or 'what happened today' in p or 'history of today' in p:
        phrase = 'history'
    # User wants to search youtube.
    if 'youtube' in p or 'video' in p or 'search youtube' in p:
        phrase = 'youtube'
    if 'email' in p or 'mail' in p:
        phrase = 'email'
    if 'website' in p or 'surf the web' in p:
        phrase = 'web'
    return phrase

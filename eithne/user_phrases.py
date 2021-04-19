def user_said(phrase):
    p = phrase
    # User asks the time.
    if 'what time is it' in p or 'what is the time' or 'time' in p or 'clock' in p:
        phrase = 'time'
    # User wants Eithne to stop listening.
    if 'turn off' in p or 'stop listening' in p or 'exit' in p or 'quit' in p:
        phrase = 'stop'
    # User wants do a google search.
    if 'search' in p or 'do a search' in p or 'google' in p or 'google search' in p:
        phrase = 'search'
    # User wants to find a location.
    if 'location' in p or 'maps' in p or 'find location' in p or 'where can i find' in p:
        phrase = 'location'
    if 'thank you' in p or 'thanks' in p or 'sound' in p or 'cheers' in p:
        phrase = 'thank'
    if 'wikipedia' in p or 'wiki' in p:
        phrase = 'wikipedia'
    if 'what is your name' in p or 'who are you' in p:
        phrase = 'name'
    return phrase

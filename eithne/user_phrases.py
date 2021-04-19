def user_said(phrase):
    # User asks the time.
    if 'what time is it' in phrase:
        phrase = 'time'
    elif 'what is the time' in phrase:
        phrase = 'time'
    elif 'time' in phrase:
        phrase = 'time'
    elif 'clock' in phrase:
        phrase = 'time'
    # User wants Eithne to stop listening.
    if 'turn off' in phrase:
        phrase = 'stop'
    elif 'stop listening' in phrase:
        phrase = 'stop'
    elif 'exit' in phrase:
        phrase = 'stop'
    elif 'thank you for your service' in phrase:
        phrase = 'stop'
    # User wants do a google search.
    if 'search' in phrase:
        phrase = 'search'
    elif 'do a search' in phrase:
        phrase = 'search'
    elif 'google' in phrase:
        phrase = 'search'
    elif 'google search' in phrase:
        phrase = 'search'
    # User wants to find a location.
    if 'location' in phrase:
        phrase = 'location'
    elif 'maps' in phrase:
        phrase = 'location'
    elif 'find location' in phrase:
        phrase = 'search'
    elif 'where can i find' in phrase:
        phrase = 'search'
    return phrase

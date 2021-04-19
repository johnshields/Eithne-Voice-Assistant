def user_said(phrase):
    # User asks the time.
    if 'what time is it' or 'what is the time' or 'time' or 'clock' in phrase:
        phrase = 'time'
    # User wants Eithne to stop listening.
    elif 'turn off' or 'stop listening' or 'exit' or 'thank you for your service' in phrase:
        phrase = 'stop'
    # User wants do a google search.
    elif 'search' or 'do a search' or 'google' or 'google search' in phrase:
        phrase = 'search'
    # User wants to find a location.
    elif 'location' or 'maps' or 'find location' or 'where can i find' in phrase:
        phrase = 'location'
    return phrase

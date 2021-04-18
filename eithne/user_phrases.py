def user_ask_for_time(phrase):
    if 'what time is it' in phrase:
        phrase = 'time'
    if 'what is the time' in phrase:
        phrase = 'time'
    if 'time' in phrase:
        phrase = 'time'
    if 'clock' in phrase:
        phrase = 'time'
    return phrase


def stop_listening(phrase):
    if 'turn off' in phrase:
        phrase = 'stop'
    if 'stop listening' in phrase:
        phrase = 'stop'
    if 'exit' in phrase:
        phrase = 'stop'
    if 'thank you for your service' in phrase:
        phrase = 'stop'
    return phrase

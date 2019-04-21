
import re

from flask import render_template, request, session


def check_trie(root, word):
    # looks up word in given trie. 
    # if already there, return True, else return False
    current = root
    for letter in word:
        try:
            current = current[letter]
        except:
            return False
    try: 
        current = current['end']
        return True
    except:
        return False


def add_trie(root, word):
    # adds word to trie
    current = root
    for letter in word:
        try:
            current = current[letter]
        except:
            current[letter] = {}
            current = current[letter]
    current['end'] = True
    return 0


def message(message, title="Attention", code=200):
    """Render message to user."""
    return render_template("message.html", title=title, message=message, code=code), code


def list_words(text):
    # returns list of words in string all lowercase
    words = re.split('\W+', text)
    return [word.lower() for word in words if word]

    


# CS0W-Project 2 - Flack
# By Kyle Chatman
#
# define helper functions 

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

# gives user an error page
def problem(message, title="Attention", code=200):
    """Render message to user."""
    session.clear()
    return render_template("problem.html", title=title, message=message, code=code), code


def list_words(text):
    # takes block of text and returns list of individual words all lowercase
    words = re.split('\W+', text)
    return [word.lower() for word in words if word]

    


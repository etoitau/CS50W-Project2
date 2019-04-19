
from flask import render_template, request, session


def addchecktrie(root, word):
    # looks up word in given trie. 
    # if already there, return True, else add it and return False
    current = root
    indict = True
    for letter in word:
        try:
            current = current[letter]
        except:
            indict = False
            current[letter] = {}
            current = current[letter]
    return indict


def message(message, title="Attention", code=200):
    """Render message to user."""
    return render_template("message.html", title=title, message=message, code=code), code
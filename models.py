# CS0W-Project 2 - Flack
# By Kyle Chatman
#
# define classes and methods 

from helpers import list_words, add_trie, check_trie

# message object
class Message:
    def __init__(self, user_name, text, time):
        self.user_name = user_name
        self.text = text
        self.time = time
        self.num_words = len(list_words(text))

# channel object
class Channel:
    def __init__(self, name):
        self.word_count = 0     # number of words that have been used up
        self.messages = list()  # list of message objects
        self.trie = {}          # trie for storing and looking up words that have been used
        self.name = name        # name of the channel

    def add_msg(self, message):
        # add message to channel at start of list
        self.messages.insert(0, message)
        # if there are now over 100 messages in channel, delete oldest
        if len(self.messages) > 100:
            del self.messages[-1]
        # add to word count
        self.word_count += message.num_words
        # add words to trie of used words
        for word in list_words(message.text):
            add_trie(self.trie, word)

    def __str__(self):
        return f'name: {self.name}, word_count: {self.word_count}, messages: {len(self.messages)}'



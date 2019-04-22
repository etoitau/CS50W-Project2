# CS50W-Project2
Web Programming with Python and JavaScript

## OnceWord

### Short Writeup 
#### From specifications:
In this project, you’ll build an online messaging service using Flask, similar in spirit to Slack. Users will be able to sign into your site with a display name, create channels (i.e. chatrooms) to communicate in, as well as see and join existing channels. Once a channel is selected, users will be able to send and receive messages with one another in real time. Finally, you’ll add a personal touch to your chat application of your choosing!

#### Personal Touch
Main added feature is a restriction to only use each word once in a particular channel. The used words are stored in a trie for quick checking

### What's in each file
    .
    ├── static                  # static files
    │   ├── chatscripts.js      # scripts that handle socketio communication and scroll handling
    │   ├── favicon.ico         # icon
    │   └── styles.css          # stylesheet
    ├── templates               # html templates
    │   ├── channels.html       # create/view channels
    │   ├── chat.html           # chat in a channel
    │   ├── layout.html         # other pages extend this. Navbar, tabs, etc
    │   ├── problem.html        # for serving error (or other) messages
    │   └── username.html       # pick a name
    ├── .gitignore              # exclude files only applicable to my machine
    ├── readme.md               # this
    ├── application.py          # main application file with routes defined
    ├── helpers.py              # some functions that application.py imports and uses 
    │                             (get manage trie structures, process text, serve error messages, etc)
    ├── models.py               # define classes and methods for custom objects (message, channel)
    └── requirements.txt        # necessary to install these to run app

### Other info
Github:
https://github.com/etoitau/CS50W-Project2
Youtube walkthrough:
https://youtu.be/YD0nKyvK9Xk
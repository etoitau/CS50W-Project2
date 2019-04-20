import os
import datetime
import logging

from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from flask.logging import create_logger
from flask_socketio import SocketIO, emit
from helpers import check_trie, list_words, message
from models import *


# set as app, set up socketio
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


# Set up logging
log = create_logger(app)
log.setLevel(logging.DEBUG)

# initialize data
testtrie = dict()
channels = dict()


@socketio.on("send_message")
def usr_message(data):
    log.info("got message")
    text = data["text"]
    user_name = data["name"]
    channel_name = data["channel"]
    time = datetime.datetime.now().strftime("%y-%m-%d, %I:%M%p")
    log.debug("in channel: %s", channel_name)
    log.debug("%s @ %r: %s", user_name, time, text)
    used_words = ""
    # iterate over words and check to do
    for word in list_words(text):
        log.debug("checking if used: %s", word)
        if check_trie(channels[channel_name].trie, word):
            used_words += " " + word
    emit("message_status", used_words)
    if not len(used_words):  
        mess = Message(user_name, text, time)
        channels[channel_name].add_msg(mess)
        json_response = {
            "message": {
                "user_name": mess.user_name,
                "text": mess.text,
                "time": mess.time
            },
            "channel": channel_name
        }
        emit("distribute_message", json_response, broadcast=True)


@app.route("/")
def index():
    log.info("index route called")
    username = session.get("username") 
    channel = session.get("channel")
    log.debug("got username: %s", username)
    log.debug("got channel: %s", channel)
    if not username:
        return redirect('/username')
    if not channel:
        return redirect('/channel')
    return redirect(url_for('chat', channel_name=channel))

@app.route("/channel", methods=["GET", "POST"])
def channel():
    if request.method == "POST":
        log.info("channel route called as POST")
        name = request.form.get("channel_name")
        log.debug("name for channel: %s", name)
        channels[name] = Channel(name)
        log.debug("new channel:")
        log.debug(channels[name])
        session['channel'] = name
        return redirect('/')
    else:    
        # serve channel page with listing
        log.info("channel route called as GET")
        username = session.get("username")
        log.debug("username: %s", username)
        channel_info = list()
        log.debug("channels:")
        log.debug(channels)
        if len(channels):
            for key, channel in channels.items():
                log.debug("channel:")
                log.debug(channel)
                channel_info.insert(0, {'name': channel.name, 'word_count': channel.word_count})
        return render_template('channels.html', channels=channel_info, username=username)


@app.route("/chat/<channel_name>")
def chat(channel_name):
    log.info("chat called with channel: %s", channel_name)
    username = session.get("username") 
    if channels[channel_name].messages:
        messages = reversed(channels[channel_name].messages)
    else: 
        messages = list()
    return render_template('chat.html', messages=messages, username=username, channel=channel_name)


@app.route("/username", methods=["GET", "POST"])
def username():
    """set username"""
    # Forget any existing
    session.clear()
    # upon submitting
    if request.method == "POST":
        log.info("username as POST")
        # Ensure username was submitted
        if not request.form.get("username"):
            return message("must provide username", "Error", 400)
        # Remember which user has logged in
        session["username"] = request.form.get("username")
        # Redirect user to home page
        return redirect("/")
    # showing up to log in
    else:
        log.info("username as GET")
        return render_template('username.html')

    
    
    
    

if __name__ == '__main__':
    socketio.run(app)
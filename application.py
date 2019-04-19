import os

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit
from helpers import addchecktrie

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

testtrie = dict()

@socketio.on("send_message")
def usr_message(data):
    text = data["text"]
    if addchecktrie(testtrie, text):
        text = "taken"
    emit("distribute_message", {"text_blast": text}, broadcast=True)


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)
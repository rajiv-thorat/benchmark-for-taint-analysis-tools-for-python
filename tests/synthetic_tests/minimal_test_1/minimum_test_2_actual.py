#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/minimal_route")
def minimal_route() -> None:
    command = request.view_args.get('command') #source
    char = Character(command)

class Character:
    def __init__(self, command):
        eval(command)
#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/dictionary_route")
def dictionary_route() -> None:
    command = request.view_args.get('command') #source
    diction = {'tainted': command, 'untainted': 'untainted value'}
    sanitized_dict = sanitize(diction)
    eval(sanitized_dict.get('tainted')) #sink, false positive

def sanitize(diction: dict) -> dict:
    sanitized_dict = {}
    valid_commands = { 'list' : 'ls', 'stats': 'stat'}
    for key in diction.keys():
        sanitized_dict[key] = valid_commands[diction.get(key)]
    return sanitized_dict
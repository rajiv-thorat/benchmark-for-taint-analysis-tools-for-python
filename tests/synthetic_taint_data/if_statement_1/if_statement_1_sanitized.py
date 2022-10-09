#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/if_route")
def if_route() -> None:
    command = request.view_args.get('operator')
    i = 10
    if i > 0:
        # This is a candidate for a false positive.
        eval(sanitize(command))

def sanitize(command: str) -> str:
    valid_commands = { 'list' : 'ls', 'stats': 'stat'}
    return valid_commands[command]
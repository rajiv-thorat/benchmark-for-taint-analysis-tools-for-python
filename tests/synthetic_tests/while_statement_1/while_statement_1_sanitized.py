#!/usr/bin/env python3
from flask import Flask, request
from random import randint

app = Flask(__name__)

@app.route("/while_route")
def while_route() -> None:
    command = request.view_args.get('operator')
    random_number = randint(1,20)
    while random_number != 0:
        random_number = random_number - 1
        # Sanitized the tainted value before use. This is a candidate for a false positive.
        eval(sanitize(command))

def sanitize(command: str) -> str:
    valid_commands = { 'list' : 'ls', 'stats': 'stat'}
    return valid_commands[command]
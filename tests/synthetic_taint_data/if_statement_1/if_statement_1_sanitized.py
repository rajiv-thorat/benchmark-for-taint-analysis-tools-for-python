#!/usr/bin/env python3
from subprocess import check_call

from flask import Flask, request
app = Flask(__name__)

@app.route("/if_route")
def if_route() -> None:
    command = request.args.get('command', '')
    i = 10
    if i > 0:
        # This sink will always be reached, but the tainted value is sanitized.
        check_call([sanitize(command)])

def sanitize(command: str) -> str:
    valid_commands = { 'list' : 'ls', 'stats': 'stat'}
    return valid_commands[command]
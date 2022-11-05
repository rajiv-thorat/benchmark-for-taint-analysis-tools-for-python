#!/usr/bin/env python3
"""  
The sanitizer in the if statement test case is inserted as a chained function call on the tainted parameter.
This test should be an easy case to detect sanitization.
"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/if_route")
def if_route() -> None:
    command = request.view_args.get('command')
    i = 10
    if i > 0:
        # This is a candidate for a false positive.
        eval(sanitize(command))

def sanitize(command: str) -> str:
    valid_commands = { 'list' : 'ls', 'stats': 'stat'}
    return valid_commands[command]
#!/usr/bin/env python3
from flask import Flask, request
from numpy import empty

app = Flask(__name__)

@app.route("/exception_route")
def exception_route() -> None:
    empty_list = empty( 7, dtype=object)
    command = ''
    try:
        command = request.view_args.get('command') #source
        if empty_list[8] == 'test value':
            command = 'problem'
    except:
        # The sink is after the exception has been caught.
        eval(command) # sink
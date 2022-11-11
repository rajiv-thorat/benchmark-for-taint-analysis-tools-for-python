#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/exception_route")
def exception_route() -> None:
    command = ''
    try:
        command = request.view_args.get('command') #source
        raise RuntimeError(command)
    except RuntimeError as ex:
        # The sink is after the exception has been caught.
        eval(ex.args) # sink
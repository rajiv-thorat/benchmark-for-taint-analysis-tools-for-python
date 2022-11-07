#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/exception_route")
def exception_route() -> None:
    command = ''
    try:
        raise RuntimeError()
        command = request.view_args.get('command') #source
    except:
        # The exception is raised before the taint is assigned to the field. This is a false positive candidate.
        eval(command) #sink, false positive
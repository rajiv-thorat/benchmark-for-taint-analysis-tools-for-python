#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/exception_route")
def exeption_route() -> None:
    command = ''
    try:
        raise RuntimeError()
        command = request.view_args.get('operator')
    except:
        # The exception is raised before the taint is assigned to the field. This is a false positive candidate.
        eval(command)
#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/exception_route")
def exeption_route() -> None:
    command = ''
    try:
        command = request.view_args.get('operator')
        raise RuntimeError()
    except RuntimeError as ex:
        # The sink is after the exception has been caught.
        eval(ex.message)
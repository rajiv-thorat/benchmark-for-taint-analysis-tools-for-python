#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/while_route")
def while_route() -> None:
    command = request.view_args.get('operator')
    while False:
        # This is dead code and a candidate for a false positive.
        eval(command)
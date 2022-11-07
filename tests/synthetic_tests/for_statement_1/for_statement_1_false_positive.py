#!/usr/bin/env python3
from flask import Flask, request
from random import randint

app = Flask(__name__)

@app.route("/for_route")
def for_route() -> None:
    command = request.view_args.get('command') #source
    for i in []:
        # The sink is inside dead code.
        eval(command) #sink, false positive

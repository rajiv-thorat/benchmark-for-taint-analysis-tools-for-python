#!/usr/bin/env python3
from flask import Flask, request
from random import randint

app = Flask(__name__)

@app.route("/while_route")
def while_route() -> None:
    command = request.view_args.get('command') #source
    random_number = randint(1,20)
    while random_number != 0:
        random_number = random_number - 1
        # The sink is inside a loop.
        eval(command) #sink
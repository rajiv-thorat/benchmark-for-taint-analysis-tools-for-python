#!/usr/bin/env python3
from flask import Flask, request
from random import randint

app = Flask(__name__)

@app.route("/if_route")
def if_route() -> None:
    command = request.view_args.get('operator')
    i = randint(1, 0)
    if i > 0:
        # The sink is inside a branch
        eval(command)
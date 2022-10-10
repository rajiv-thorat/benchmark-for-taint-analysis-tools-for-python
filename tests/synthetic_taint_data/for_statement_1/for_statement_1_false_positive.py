#!/usr/bin/env python3
from flask import Flask, request
from random import randint

app = Flask(__name__)

@app.route("/for_route")
def for_route() -> None:
    command = request.view_args.get('operator')
    random_number = randint(0,0)
    for i in range(random_number):
        # The sink is inside dead code. Candidate for false positive.
        eval(command)

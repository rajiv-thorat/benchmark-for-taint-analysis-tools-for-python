#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/if_route")
def if_route() -> None:
    command = request.view_args.get('operator')
    i = 10
    if i < 0:
        eval(command)

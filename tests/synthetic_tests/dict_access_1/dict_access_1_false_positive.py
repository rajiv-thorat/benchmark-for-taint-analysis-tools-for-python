#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/dictionary_route")
def dictionary_route() -> None:
    command = request.view_args.get('operator')
    diction = {'tainted': command, 'untainted': 'untainted value'}
    eval(diction.get('untainted'))
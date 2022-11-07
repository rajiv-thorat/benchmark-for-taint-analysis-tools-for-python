#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/array_to_string_route")
def array_to_string_route() -> None:
    command = request.view_args.get('command') #source
    array_1 = ['element 1', command]
    eval(array_1.__str__()) # sink
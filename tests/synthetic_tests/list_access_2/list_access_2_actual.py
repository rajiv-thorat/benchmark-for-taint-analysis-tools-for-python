#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/array_route")
def array_route() -> None:
    command = request.view_args.get('operator')
    new_array = []
    new_array.append('list')
    new_array.append(command)
    new_array.append('ls')
    eval(new_array[calculate_index()])

def calculate_index():
    return random.randint(0, 2)
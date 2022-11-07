#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/function_call")
def function_call() -> None:
    command = request.view_args.get('command') #source
    function_a(command)

def function_a(command):
    eval(command) # sink
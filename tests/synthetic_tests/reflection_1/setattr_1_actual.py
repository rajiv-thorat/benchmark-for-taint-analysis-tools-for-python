#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

class ClassA:
    def __init__(self):
        print('Adding stuff to not have an empty class.')
        
@app.route("/minimal_route")
def minimal_route() -> None:
    command = request.view_args.get('command')
    instance_a = ClassA()
    setattr(instance_a, 'command', command)
    eval(instance_a.command)

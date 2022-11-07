#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

class ClassA:
    def __init__(self):
        print('Adding stuff to not have an empty class.')
        
@app.route("/reflection_route")
def reflection_route() -> None:
    command = request.view_args.get('command') #source
    instance_a = ClassA()
    setattr(instance_a, 'command', command)
    eval(instance_a.command) #sink

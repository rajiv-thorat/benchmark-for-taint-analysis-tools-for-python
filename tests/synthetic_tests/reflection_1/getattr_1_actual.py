#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

class ClassA:
    command = ''
    
@app.route("/reflection_route")
def reflection_route() -> None:
    command = request.view_args.get('command') #source
    instance_a = ClassA()
    instance_a.command = command
    eval(getattr(instance_a, 'command')) #sink

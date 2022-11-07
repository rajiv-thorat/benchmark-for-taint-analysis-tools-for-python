#!/usr/bin/env python3
from flask import Flask, request
from class_a import ClassA

app = Flask(__name__)

@app.route("/object_route")
def object_route() -> None:
    command = request.view_args.get('operator')
    instance_1 = ClassA()
    instance_1.command = command

    command = 'list'
    instance_1.command = 'ls'
    
    eval(command)
    eval(instance_1.command)
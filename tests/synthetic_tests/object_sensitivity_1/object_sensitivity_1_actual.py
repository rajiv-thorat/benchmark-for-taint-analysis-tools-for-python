#!/usr/bin/env python3
from flask import Flask, request
from class_a import ClassA

app = Flask(__name__)

@app.route("/object_route")
def object_route() -> None:
    command = request.view_args.get('command') #source
    instance_1 = ClassA()
    instance_2 = ClassA()

    instance_1.set_command(command)
    instance_2.set_command('list')
    eval(instance_1.get_command) # sink
#!/usr/bin/env python3
from flask import Flask, request
from class_a import ClassA

app = Flask(__name__)

@app.route("/if_route")
def if_route() -> None:
    command = request.view_args.get('operator')
    instance_1 = ClassA()
    instance_2 = ClassA()

    instance_1.set_command(command)
    instance_2.set_command('list')
    eval(instance_2.get_command)
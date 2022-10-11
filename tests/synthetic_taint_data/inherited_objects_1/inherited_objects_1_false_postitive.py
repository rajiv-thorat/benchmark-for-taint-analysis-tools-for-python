#!/usr/bin/env python3
from flask import Flask, request
from sub_class_a import SubClassA
from sub_class_b import SubClassB

app = Flask(__name__)

@app.route("/inheritance_route")
def inheritance_route() -> None:
    command = request.view_args.get('operator')
    condition = 10 + 1
    instance = None
    if condition == 10:
        instance = SubClassA()
        instance.set_command(command)
    else:
        instance = SubClassB()
        instance.set_command('list')
    eval(instance.get_command())

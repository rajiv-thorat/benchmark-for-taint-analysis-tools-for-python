#!/usr/bin/env python3
from flask import Flask, request
from class_a import ClassA
from class_b import ClassB

app = Flask(__name__)

def factory(class_name: str):
    factories = {
        "ClassA": ClassA,
        "ClassB": ClassB
    }
    return factories[class_name]()

@app.route("/factory_route")
def factory_route() -> None:
    command = request.view_args.get('operator')
    a = factory("ClassA")
    a.set_command(command)
    eval(a.get_command())
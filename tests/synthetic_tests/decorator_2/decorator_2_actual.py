#!/usr/bin/env python3
"""  
In this test case we check the support for decorators. The method decorator_route() contains the source and is wrapped in the TaintedDecorator.
The sink is in the __call__ function of class TaintedDecorator. This decorator is the class type.
"""
from flask import Flask, request

app = Flask(__name__)

class TaintedDecorator:
    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        command = self.function(*args, **kwargs)
        eval(command) # sink

@TaintedDecorator
@app.route("/decorator_route")
def decorator_route() -> None:
    command = request.view_args.get('command') #source
    return command
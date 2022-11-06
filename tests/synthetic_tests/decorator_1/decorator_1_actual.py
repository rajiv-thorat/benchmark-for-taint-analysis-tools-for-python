#!/usr/bin/env python3
""" 
In this test case we check the support for decorators. The method decorator_route() contains the source and is wrapped in the tainted_decorator.
The sink is in the tainted_decorator. This decorator is is the function type.
"""
from flask import Flask, request

app = Flask(__name__)

def tainted_decorator(funct):
    command = func(*args, **kwargs)
    eval(command)
    
@tainted_decorator
@app.route("/decorator_route")
def decorator_route() -> None:
    command = request.view_args.get('command')
    return command

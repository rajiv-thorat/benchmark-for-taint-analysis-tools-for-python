#!/usr/bin/env python3
""" 
The abstract factory design pattern is a way to encapsulate a group of objects with a common
theme without the concrete class. In this test case , the
objects are initialized at runtime and returned by the function factory(). The get_command() 
function in ClassA returns the command field as it is set, i.e., the taint is propagated. The
get_command() function of ClassB, on the other hand, returns a constant string, i.e., breaking
any taint flow. Which object is created at runtime will be difficult for static analysis to determine.
This test includes sanitization.
"""
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
    command = request.view_args.get('command') #source
    a = factory("ClassA")
    a.set_command(command)
    eval(a.get_command_sanitized()) # sink, false positive
#!/usr/bin/env python3
from class_a import ClassA
from class_b import ClassB
import random
from flask import Flask, request

app = Flask(__name__)

@app.route("/aliasing_route")
def aliasing_route() -> None:
    a = ClassB()
    p = ClassB()

    b = ClassA()
    q = ClassA()

    if True:
        x = a
        y = b
    else:
        x = p
        y = q

    x.a_instance = y
    q.random_data = request.view_args.get('command') #source
    eval(a.a_instance.random_data) #sink, false positive
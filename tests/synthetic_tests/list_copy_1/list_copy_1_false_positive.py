#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/array_copy_route")
def array_copy_route() -> None:
    command = request.view_args.get('command') #source
    array_1 = ['element 1', command]
    array_2 = ['element 3', 'element 4', array_1[0]]

    eval(array_2[2]) #sink, false positive
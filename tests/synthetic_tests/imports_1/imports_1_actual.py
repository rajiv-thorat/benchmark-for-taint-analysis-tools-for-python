#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/import_route")
def import_route() -> None:
    command = request.view_args.get('command') #source
    imported = __import__('class_a' , globals(), locals(), [], 0)
    instance_a = imported.ClassA()
    instance_a.evaluate(command)

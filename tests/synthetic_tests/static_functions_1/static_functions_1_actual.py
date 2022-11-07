#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

class ClassA:
    @staticmethod
    def evaluate(self, command):
        eval(command) #sink

@app.route("/static_route")
def static_route() -> None:
    command = request.view_args.get('command') #source
    ClassA.evaluate(command)
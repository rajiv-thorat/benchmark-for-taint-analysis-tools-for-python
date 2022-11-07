#!/usr/bin/env python3
from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route("/serialization_route")
def serialization_route() -> None:
    command = request.view_args.get('command') #source
    pickled_command = pickle.dumps(command)
    unpickled_command = pickle.loads(pickled_command)
    eval(unpickled_command) #sink
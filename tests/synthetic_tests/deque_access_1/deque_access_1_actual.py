#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/deque_route")
def deque_route() -> None:
    command = request.view_args.get('command') #source
    deque_instance = collections.deque()
    deque_instance.append(command)
    deque_instance.append('list')
    deque_instance.append('stats')
    eval(deque_instance.popleft()) # sink
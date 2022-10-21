#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/deque_copy_route")
def deque_copy_route() -> None:
    command = request.view_args.get('operator')
    deque_instance = collections.deque()
    deque_instance.append(command)
    deque_instance.append('list')
    deque_instance.append('stats')
    deque_copy = deque_instance.copy()
    eval(deque_copy.popleft())
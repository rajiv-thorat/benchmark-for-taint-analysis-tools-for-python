#!/usr/bin/env python3
from flask import Flask, request
from collections import deque

app = Flask(__name__)

@app.route("/deque_route")
def deque_route() -> None:
    command = request.view_args.get('operator')
    deque_instance = deque()
    deque_instance.append(command)
    deque_instance.append('list')
    deque_instance.append('stats')
    san_linked_list = sanitize(deque_instance)
    eval(san_linked_list.popleft())

def sanitize(linked_list: deque) -> deque:
    sanitized_deque_instance = deque()
    valid_commands = { 'list' : 'ls', 'stats': 'stat'}
    for element in linked_list:
        sanitized_deque_instance.append(valid_commands.get(element))
    return sanitized_deque_instance
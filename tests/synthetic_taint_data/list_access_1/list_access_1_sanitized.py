#!/usr/bin/env python3
from flask import Flask, request
from collections import deque

app = Flask(__name__)

@app.route("/list_route")
def list_route() -> None:
    command = request.view_args.get('operator')
    linked_list = deque()
    linked_list.append(command)
    linked_list.append('list')
    linked_list.append('stats')
    san_linked_list = sanitize(linked_list)
    eval(san_linked_list.popleft())

def sanitize(linked_list: deque) -> deque:
    sanitized_linked_list = deque()
    valid_commands = { 'list' : 'ls', 'stats': 'stat'}
    for element in linked_list:
        sanitized_linked_list.append(valid_commands.get(element))
    return sanitized_linked_list
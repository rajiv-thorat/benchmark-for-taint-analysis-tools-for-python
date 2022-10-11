#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/list_copy_route")
def list_copy_route() -> None:
    command = request.view_args.get('operator')
    linked_list = collections.deque()
    linked_list.append(command)
    linked_list.append('list')
    linked_list.append('stats')
    linked_list_copy = linked_list.copy()
    eval(linked_list_copy.popleft())
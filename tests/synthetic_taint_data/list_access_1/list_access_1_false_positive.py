#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/list_route")
def list_route() -> None:
    command = request.view_args.get('operator')
    linked_list = collections.deque()
    linked_list.append('list')
    linked_list.append(command)
    linked_list.append('stats')
    eval(linked_list.popleft())
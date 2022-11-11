#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/exec_route")
def exec_route() -> None:
    taint_flow = '''
    command = request.view_args.get('command') #source
    eval(command) # sink
    '''
    exec(taint_flow)
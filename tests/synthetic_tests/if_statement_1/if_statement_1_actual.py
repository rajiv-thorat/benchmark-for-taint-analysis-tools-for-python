#!/usr/bin/env python3
""" 
This is an example of one of the most straightforward test cases. 
It is built on the if statement.
This test checks whether the analyses performed by the tools can handle branching that is decided at runtime.
Since the execution of the path to the sink can only be decided at runtime, the analyses must include the branch, i.e., detect a taint flow.
"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/if_route")
def if_route() -> None:
    command = request.view_args.get('command') #source
    if True:
        # The sink is inside a branch
        eval(command) # sink
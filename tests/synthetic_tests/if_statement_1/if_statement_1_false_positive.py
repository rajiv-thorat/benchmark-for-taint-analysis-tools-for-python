#!/usr/bin/env python3
"""  
The false positive test case designed around the if statement checks for the detection of dead code or unreachable code.
The condition for the branch is always false, i.e., the sink is dead or unreachable code.
This detection of dead code will confirm if the analyses are path-sensitive.
"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/if_route")
def if_route() -> None:
    command = request.view_args.get('command') #source
    if False:
        # This is dead code.
        eval(command) #sink, false positive
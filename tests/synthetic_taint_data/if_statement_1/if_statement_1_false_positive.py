#!/usr/bin/env python3
from subprocess import check_call
from os import popen, system

from flask import Flask, request
app = Flask(__name__)

@app.route("/if_route")
def if_route() -> None:
    command = request.args[1]
    i = 10
    #if i < 0:
    if i > 0:
        # This sink is dead code
        check_call([command])
        eval(command)
        exec(command)
        popen(command)
        system(command)

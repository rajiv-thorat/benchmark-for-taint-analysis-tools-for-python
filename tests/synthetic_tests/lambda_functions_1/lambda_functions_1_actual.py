#!/usr/bin/env python3
"""  
This test checks whether the tools can work with lambda expressions. 
The source is a lambda function, and the the tainted data is passed to it.
"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/lambda_route")
def lambda_route() -> None:
    lambda_function = lambda param: request.view_args.get(param)
    command = lambda_function('command')
    eval(command)
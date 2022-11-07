#!/usr/bin/env python3
"""  
This test checks whether the tools can work with lambda expressions. 
The sink is a lambda function, and the the tainted data is passed to it.
"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/lambda_route")
def lambda_route() -> None:
    command = request.view_args.get('command')
    lambda_function = lambda comm : eval(comm)
    lambda_function(command)
#!/usr/bin/env python3
from flask import Flask, request
from sub_class_a import SubClassA
from sub_class_b import SubClassB

app = Flask(__name__)

@app.route("/inheritance_route")
def inheritance_route() -> None:
    command = request.view_args.get('operator')
    instance = SubClassA(command)
    instance = SubClassB('list')
    eval(instance.get_command())

#!/usr/bin/env python3
from flask import Flask, request
import numpy

app = Flask(__name__)

@app.route("/multi_array_route")
def multi_array_route() -> None:
    command = request.view_args.get('command') #source
    multi_dem = numpy.array([command, 'element 1'],['element 2', 'element 3'])
    source_item = multi_dem[0,0]
    eval(source_item) # sink
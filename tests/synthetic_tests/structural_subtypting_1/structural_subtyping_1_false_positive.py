#!/usr/bin/env python3
"""  
This test case check if the tools can work with duck typing. The sink is in class ClassB. The function sink is called from the function evaluate.
Which one of the classes is used depends on the instance passed to the evaluate function. In this case, the tainted data is passed to the evaluate function,
then to the Proto Class, and ends with the sink function from the class ClassB.
"""

from flask import Flask, request

app = Flask(__name__)

class Proto(Protocol):
    def sink(self, command):
        ...

def evaluate(instance:Proto, command):
    instance.sink(command)

class ClassA:
    def sink(self, command):
        eval('list')

class ClassB:
    def sink(self, command):
        eval(command) #sink, false positive

@app.route("/duck_route")
def duck_route() -> None:
    command = request.view_args.get('command') #source
    evaluate(ClassA(), command)
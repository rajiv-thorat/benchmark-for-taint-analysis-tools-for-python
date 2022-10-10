#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

class WithStatement:
    def __init__(self, command):
        self.command = command
      
    def __enter__(self):
        print("Entered the __enter__ method")
  
    def __exit__(self, exception_type, exception_value, traceback):
        print("Entered the __exit__ method")
    
    def print_len(self):
        print(self.command)
        # The sink is inside the called function
        eval(self.command)

@app.route("/with_route")
def with_route() -> None:
    command = request.view_args.get('operator')
    # The tainted value was sanitized before passing on to the class. Candidate for a false positive.
    with WithStatement(sanitize(command)) as instance:
        # The sink is inside a loop.
        instance.print_len()
    
def sanitize(command: str) -> str:
    valid_commands = { 'list' : 'ls', 'stats': 'stat'}
    return valid_commands[command]
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
        print("Entered the print_len method")

@app.route("/while_route")
def while_route() -> None:
    command = request.view_args.get('operator')
    with WithStatement(command) as instance:
        instance.print_len()
        # The sink is inside the with scope, and sanitized. This is a candidate for a false positive
        eval(sanitize(command))

def sanitize(command: str) -> str:
    valid_commands = { 'list' : 'ls', 'stats': 'stat'}
    return valid_commands[command]
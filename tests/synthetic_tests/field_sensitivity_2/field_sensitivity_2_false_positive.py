 #!/usr/bin/env python3
from flask import Flask, request
from character import Character

app = Flask(__name__)

@app.route("/field_sensitivity_route")
def field_sensitivity_route() -> None:
    command = request.view_args.get('command') #source
    char = Character()
    char.set_name = 'name'
    char.set_path(command)
    # Accessing a field other than the tainted one.
    eval(char.get_name())    #sink, false positive
    
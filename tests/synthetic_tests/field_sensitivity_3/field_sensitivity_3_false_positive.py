 #!/usr/bin/env python3
from flask import Flask, request
from character import Character

app = Flask(__name__)

@app.route("/field_sensitivity_route")
def field_sensitivity_route() -> None:
    command = request.view_args.get('operator')
    char = Character()
    char.set_name = 'name'
    char.set_path('')
    eval(char.get_path())   
    # The taint is set after the possible sink is called. This is a false positive candidate.
    char.set_path(command)
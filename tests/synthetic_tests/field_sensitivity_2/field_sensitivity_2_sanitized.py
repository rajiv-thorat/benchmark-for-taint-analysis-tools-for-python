 #!/usr/bin/env python3
from flask import Flask, request
from character import Character

app = Flask(__name__)

@app.route("/field_sensitivity_route")
def field_sensitivity_route() -> None:
    command = request.view_args.get('operator')
    char = Character()
    char.set_name = 'name'
    char.set_path(command)
    fixed_char_path = ''
    if  (['list', 'args'].__contains__(char.get_path())):
        fixed_char_path = char.get_path()
    # The tainted field is passed after sanitization.
    eval(fixed_char_path)   
    
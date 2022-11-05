# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from subprocess import run

from os import popen, system
from flask import Flask, request

app = Flask(__name__)

@app.route("/rce/<string:payload>")
def definite_rce(payload: str) -> None:
    run(payload, shell=True)

@app.route("/if_route")
def if_route() -> None:
    command = request.view_args.get('operator')
    i = 10
    #if i < 0:
    if i > 0:
        # This sink is dead code
        check_call([command])
        eval(command)
        exec(command)
        popen(command)
        system(command)
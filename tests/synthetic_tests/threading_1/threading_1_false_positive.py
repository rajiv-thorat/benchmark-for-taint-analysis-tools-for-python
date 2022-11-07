#!/usr/bin/env python3
from flask import Flask, request
from threading import Thread

app = Flask(__name__)

@app.route("/threading_route")
def threading_route() -> None:
    command = request.view_args.get('command') #source
    thread_1 = Thread(target=eval, args=['ls']) #sink, false positive
    thread_1.run()

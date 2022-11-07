#!/usr/bin/env python3
from flask import Flask, request
from threading import Thread

app = Flask(__name__)

@app.route("/threading_route")
def threading_route() -> None:
    command = request.view_args.get('command')
    thread_1 = Thread(target=eval, args=[command])
    thread_1.run()

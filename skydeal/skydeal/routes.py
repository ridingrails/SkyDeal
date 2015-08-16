#!/usr/bin/env python3

from skydeal import app
#put routes here

@app.route('/')
def index():
    return "Hello World!"

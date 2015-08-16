#!/usr/bin/env python3

from flask import jsonify
from skydeal import app
#put routes here

@app.route('/offers')
def offers():
    return jsonify(**{"r":"Offers"})



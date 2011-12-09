#! /usr/bin/env python
"""The main application logic for PyTips."""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!\n'

if __name__ == '__main__':
    app.run(debug=True)

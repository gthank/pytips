#! /usr/bin/env python
"""The main application logic for PyTips."""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import json
import random

from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def index():
    my_params = {
        "q": "#python+tip",
        "window": "a",
        "type": "tweet"
    }
    r = requests.get('http://otter.topsy.com/search.json', params=my_params)
    response = json.loads(r.content)['response']
    # TODO Go beyond the first page of results.
    return random.choice(response['list'])[u'title']

if __name__ == '__main__':
    app.run(debug=True)

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
QUERY = "#python+tip"
PER_PAGE = 100
SEARCH_COUNT_URL = 'http://otter.topsy.com/searchcount.json'
SEARCH_URL = 'http://otter.topsy.com/search.json'


def _get_page_and_index_for_random_tip():
    initial_count_params = {
        "q": QUERY
    }
    r = requests.get(SEARCH_COUNT_URL, params=initial_count_params)
    response = json.loads(r.content)['response']
    total_result_count = response['a']
    random_index = random.randint(0, total_result_count - 1)
    # Relies on int division truncating; this might be a Python 3 problem.
    page_for_random_index = random_index / PER_PAGE
    offset = PER_PAGE * page_for_random_index
    index_on_page = random_index % PER_PAGE
    return offset, index_on_page


@app.route('/')
def index():
    offset, index = _get_page_and_index_for_random_tip()
    search_params = {
        "q": QUERY,
        "window": "a",
        "offset": offset,
        "perpage": PER_PAGE,
    }
    r = requests.get(SEARCH_URL, params=search_params)
    response = json.loads(r.content)['response']
    return response['list'][index]['title']


if __name__ == '__main__':
    app.run(debug=True)

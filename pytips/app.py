#! /usr/bin/env python
"""The main application logic for PyTips."""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import json
import random

from flask import Flask, render_template
import requests


app = Flask(__name__)
SHARED_QUERY_PARAMS = {
    "q": "#python+tip",
    "window": "a",
    "allow_lang": "en",
    "type": "tweet",
}
PER_PAGE = 100
SEARCH_COUNT_URL = 'http://otter.topsy.com/searchcount.json'
SEARCH_URL = 'http://otter.topsy.com/search.json'


def _get_offset_and_index_for_random_tip():
    r = requests.get(SEARCH_COUNT_URL, params=SHARED_QUERY_PARAMS.copy())
    response = json.loads(r.content)['response']
    total_result_count = response['a']
    random_index = random.randint(0, total_result_count - 1)
    # Relies on int division truncating; this might be a Python 3 problem.
    page_for_random_index = random_index / PER_PAGE
    offset = PER_PAGE * page_for_random_index
    index_on_page = random_index % PER_PAGE
    return offset, index_on_page


def _get_tip():
    offset, index = _get_offset_and_index_for_random_tip()
    search_params = SHARED_QUERY_PARAMS.copy()
    search_params.update({
        "offset": offset,
        "perpage": PER_PAGE,
    })
    r = requests.get(SEARCH_URL, params=search_params)
    search_results = json.loads(r.content)['response']['list']
    # Although this shouldn't be happening, it addresses a real issue I was
    # experiencing.
    if index >= len(search_results):
        return _get_tip()
    full_result = search_results[index]
    return render_template('index.html',
                           url=full_result["trackback_permalink"],
                           title=full_result.get("title", None),
                           content=full_result.get("content", None),
                           author=full_result["trackback_author_nick"])


@app.route('/')
def index():
    return _get_tip()


if __name__ == '__main__':
    app.run(debug=True)

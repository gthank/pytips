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


def _format_tweet_into_tip(tweet_info):
    # TODO Figure out the *RIGHT* way to handle the Title/Content thing.
    title = tweet_info["title"]
    content = tweet_info["content"]
    if title == content:
        my_tip = title
    else:
        my_tip = '<span class="tip_title">' + title + "</span> " + content

    return '<q cite="{url}">{tip}</q>&mdash;<a href="{url}" title="The source of this tip">{author}</a>'.format(
        url = tweet_info["trackback_permalink"],
        tip = my_tip,
        author = tweet_info["trackback_author_nick"])


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
    return _format_tweet_into_tip(search_results[index])


@app.route('/')
def index():
    return _get_tip()


if __name__ == '__main__':
    app.run(debug=True)

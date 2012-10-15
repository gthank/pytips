#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""The main application logic for PyTips."""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

import codecs
import json
import random

from flask import Flask, render_template
import requests
from werkzeug.utils import unescape


utf8_encode = codecs.getencoder('UTF-8')
SHARED_QUERY_PARAMS = {
    "q": "#python+tip",
    "window": "a",
    "allow_lang": "en",
    "type": "tweet",
}
PER_PAGE = 100
SEARCH_URL = 'http://otter.topsy.com/search.json'


def create_app():
    """Create the PyTips app."""
    app = Flask(__name__)
    app.config.from_object(__name__)

    @app.route('/')
    def index():
        return _get_tip()

    def _get_offset_and_index_for_random_tip():
        search_params = SHARED_QUERY_PARAMS.copy()
        r = requests.get(SEARCH_URL, params=search_params)
        response_json = json.loads(r.content)
        app.logger.debug("The results we use for counting purposes:\n%s",
                         response_json)
        total_result_count = response_json['response']['total']
        random_index = random.randint(0, total_result_count - 1)
        page_for_random_index = random_index // PER_PAGE
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
        response_json = json.loads(r.content)
        app.logger.debug("Here are our search results:\n%s", response_json)
        search_results = response_json['response']['list']
        full_result = search_results[index]
        app.logger.debug("Here is the tweet to use as the tip:\n%s", full_result)
        title = full_result.get("title", None)
        content = full_result.get("content", None)
        # OtterAPI gives us escaped strings, but Jinja will handle any needed
        # escaping, so we'll have Werkzeug unescape them for us.
        # Werkzeug's unescape requires us to give it a buffer or str object,
        # not a Unicode, so we need to encode it to bytes; we know it's
        # UTF-8 because that's the only valid encoding for JSON.
        if content:
            encoded_content, length = utf8_encode(content)
            content = unescape(encoded_content)
        if title:
            encoded_title, length = utf8_encode(title)
            title = unescape(encoded_title)
        return render_template('index.html',
                               url=full_result["trackback_permalink"],
                               title=title,
                               content=content,
                               author=full_result["trackback_author_nick"])


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

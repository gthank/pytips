#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Primary setup for PyTips."""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division


import os


from flask import Flask


app = Flask(__name__)
app.config.from_object('pytips.default_settings')
if 'PYTIPS_SETTINGS' in os.environ:
    app.config.from_envvar('PYTIPS_SETTINGS')


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()

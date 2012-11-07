#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Primary setup for PyTips."""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division


import os


from flask import Flask
from flask_heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('pytips.default_settings')
heroku = Heroku(app)
# Flask-Heroku is looking at an env var that I don't have, so overwrite
# it with one that I found by dumping os.environ in a log statement.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'HEROKU_POSTGRESQL_CRIMSON_URL',
    app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)


# I'm about to import a module that I won't use explicitly; when it loads, the
# model definitions created, so you *must* leave the import in place. Also, it
# relies on `db` being already configured, so don't import it before everything
# is all set up.
from pytips import models
# I'm about to import a module that I won't use explicitly; when it loads, the
# routes for the app will be defined, so you *must* leave the import in place.
# Also, it relies on `app` being already configured, so don't import it before
# everything is all set up.
from pytips import views


if __name__ == '__main__':
    app.run()

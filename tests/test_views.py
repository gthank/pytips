#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the view tier in PyTips.
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division


import json
from os import path, environ
import unittest
from flask.ext.testing import TestCase
from dateutil.parser import parse as parse_date


# Before we go importing pytips (which configures everything), we need
# to *make sure* we're pointing at a nice, clean SQLite DB.
environ['DATABASE_URL'] = 'sqlite:////'
import pytips
from pytips.models import Tip


class TestViews(TestCase):
    """Test *ALL* the Views!"""
    def setUp(self):
        # Load some sample data.
        with open(path.join(path.dirname(__file__), "bootstrap.json")) as fixtures:
            fixtures_json = json.loads(fixtures.read())
            for tip_dict in fixtures_json:
                tip_dict['publication_date'] = parse_date(tip_dict['publication_date'])
            fixtures_models = (Tip(**tip) for tip in fixtures_json)
            pytips.db.session.add_all(fixtures_models)
            pytips.db.session.commit()

    def tearDown(self):
        # Delete the sample data (so the next test can reload it).
        map(pytips.db.session.delete, Tip.query.all())
        pytips.db.session.commit()

    def create_app(self):
        """Creates an instance of PyTips for testing."""
        app = pytips.app
        app.config['TESTING'] = True
        return app

    def test_index(self):
        """Test the index page ("/")."""
        self.assert200(self.client.get("/"))


if __name__ == '__main__':
    unittest.main()

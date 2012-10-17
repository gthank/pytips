"""
Tests for the view tier in PyTips.
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division


import unittest
from flask.ext.testing import TestCase


import pytips


class TestViews(TestCase):
    """Test *ALL* the Views!"""
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

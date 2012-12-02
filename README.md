# PyTips

## The Point

This is a simple example application for demonstrating some modern
practices for managing your Python project: using [`pip`][pip_home] to
manage your dependencies, writing your docs in [Sphinx][sphinx_home],
hosting your code on [bitbucket][bitbucket_home], using
[Travis CI][travisci_home] for continuous integration, hosting your
docs on [Read the Docs][rtd_home], running the actual service on
[Heroku][heroku_home], and publishing it on [PyPI][pypi] (see
[The Hitchhiker's Guide to Packaging][packaging_guide] for details).

[pip_home]: http://www.pip-installer.org/en/latest/index.html
[bitbucket_home]: https://bitbucket.org/
[rtd_home]: http://readthedocs.org/
[heroku_home]: http://www.heroku.com/
[sphinx_home]: http://sphinx.pocoo.org/
[travisci_home]: http://travis-ci.org/
[pypi]: http://pypi.python.org/pypi
[packaging_guide]: http://guide.python-distribute.org/quickstart.html

## The Implementation

The actual functionality of the app is straight-forward: it's a web application
that displays a random Python tip every time you visit the page (properly
attributed, of course). To power the site, I use [Flask][flask_home]
and [SQLAlchemy][sqlalchemy_home].

[flask_home]: http://flask.pocoo.org/
[sqlalchemy_home]: http://www.sqlalchemy.org/

## Roadmap

NOTE: This is highly tentative. Any or all of these things may never
happen, and certainly not in a timely fashion.

* Create a repeatable process for updating the set of Tips using Twitter.
* Expose said process through a Flask-Script command (or similar).
* Redesign the site.
* Package and publish the app to PyPI.
* Write some decent docs and post them to Read the Docs.
* Use pjax to request another random tip in-place.
* Create an HTML5 app for smart phones.

## Build Status

[![Build Status](https://secure.travis-ci.org/gthank/pytips.png?branch=master)](http://travis-ci.org/gthank/pytips)

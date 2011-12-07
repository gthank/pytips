# PyTips

## The Point

This is a simple example application for demonstrating some modern practices
for managing your Python project: using [`pip`][pip_home] to manage your
dependencies, writing your docs in [Sphinx][sphinx_home], hosting your code
on [bitbucket][bitbucket_home], hosting your docs on
[Read the Docs][rtd_home], and running the actual service on
[ep.io][epio_home]. As a stretch goal, it will demonstrate how to use
[Shining Panda][shiningpanda_home] for continuous integration.

[pip_home]: http://www.pip-installer.org/en/latest/index.html
[bitbucket_home]: https://bitbucket.org/
[rtd_home]: http://readthedocs.org/
[epio_home]: http://ep.io/
[sphinx_home]: http://sphinx.pocoo.org/
[shiningpanda_home]: https://www.shiningpanda.com/

## The Implementation

The actual functionality of the app is straight-forward: it's a web application
that displays a random Python tip every time you visit the page (properly
attributed, of course). To power the site, I'll be using [Flask][flask_home].
To provide the initial tips, I'll be scraping Twitter on every request.
Obviously, this could be improved. With any luck, I'll actually implement some
of those possible improvements.

[flask_home]: http://flask.pocoo.org/


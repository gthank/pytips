.. _installation:

Installation
============

PyTips is packaged using ``distutils`` and published on `PyPI <http://pypi.python.org/pypi>`_, so you can
theoretically install it using `pip <http://www.pip-installer.org/en/latest/index.html>`_, but it is still
in the alpha stage, so you're probably better off cloning from Bitbucket
and running that::

    hg clone ssh://hg@bitbucket.org/gthank/pytips
    cd pytips
    pip install -r requirements.txt

Fair warning: I generate that requirements file by running ``pip freeze`` and
doing *very* minimal cleanup, so until I cut an official release, it will
probably contain helpful tools that aren't strictly necessary for running
PyTips.

.. _virtualenv:

virtualenv
----------

PyTips plays nicely with ``virtualenv``, and I **HIGHLY** recommend you use it.


# -*- coding: utf-8 -*-
"""Utility functions for PyTips."""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division


import logging
import signal


from decorator import decorator
import html5lib
from dateutil.parser import parse as parse_date


def extract_publication_date(html):
    """Extract publish date from ``html``; assumes it's like an embedded tweet.

    :param html: a ``string`` containing HTML resembling an embedded tweet
    :rtype: ``datetime``
    """
    root = html5lib.parse(html, treebuilder='lxml', namespaceHTMLElements=False)
    publication_date_string = None
    date_anchor_nodes = root.xpath("//a/@data-datetime")
    if date_anchor_nodes:
        publication_date_string = date_anchor_nodes[0]
    else:
        date_anchor_nodes = root.xpath("//a")
        if date_anchor_nodes:
            publication_date_string = date_anchor_nodes[-1].text
    if not publication_date_string:
        logging.warn("We were unable to extract a publication date from:\n%s", html)
        return None
    return parse_date(publication_date_string)


# The following block of code was inspired by http://code.activestate.com/recipes/307871-timing-out-function/
class TimedOutException(Exception):
    """Raised when a function times out."""
    def __init__(self, value = "Timed Out"):
        super(TimedOutException, self).__init__()
        self.value = value

    def __str__(self):
        return repr(self.value)


def timeout(s):
    """Prevent a function from running more than ``s`` seconds.

    :param s: the amount of time (in seconds) to let the function attempt to finish
    """
    def _timeout(f, *args, **kwargs):
        def handle_timeout(signal_number, frame):
            raise TimedOutException

        # Grab a handle to the old alarm.
        old = signal.signal(signal.SIGALRM, handle_timeout)

        # Start our timeout logic.
        signal.alarm(s)
        try:
            result = f(*args, **kwargs)
        finally:
            # Put the old stuff back
            old = signal.signal(signal.SIGALRM, old)

        # Wipe out all alarms.
        signal.alarm(0)

        return result
    return decorator(_timeout)

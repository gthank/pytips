# -*- coding: utf-8 -*-
"""Utility functions for PyTips."""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division


import html5lib
from dateutil.parser import parse as parse_date


def extract_publication_date(html):
    """Extract publish date from ``html``; assumes it's like an embedded tweet."""
    root = html5lib.parse(html, treebuilder='lxml', namespaceHTMLElements=False)
    publication_date_string = root.xpath("//a/@data-datetime")[0]
    return parse_date(publication_date_string)

# -*- coding: utf-8 -*-
"""Define the views for PyTips."""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division


from flask import Markup, render_template
from sqlalchemy import func


from pytips import app
from pytips.models import Tip


@app.route('/')
def index():
    random_tip = Tip.query.order_by(func.random()).first()
    tip_html = random_tip.rendered_html if random_tip else "Hello, world!"
    return render_template('index.html', tip_html=Markup(tip_html))

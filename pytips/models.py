# -*- coding: utf-8 -*-
"""Defines the model 'layer' for PyTips."""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division


from sqlalchemy import func
from flask.ext.sqlalchemy import BaseQuery


from pytips import db


class TipQuery(BaseQuery):
    def random_tip(self):
        """Retrieve a random ``Tip``."""
        return self.order_by(func.random()).first()


class Tip(db.Model):
    """Represents a 'tip' for display."""
    query_class = TipQuery

    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String, nullable=False)
    author_url = db.Column(db.String(1024), nullable=False)
    url = db.Column(db.String(1024), unique=True, nullable=False)
    rendered_html = db.Column(db.String(1024), unique=True, nullable=False)
    publication_date = db.Column(db.DateTime(timezone=True), nullable=False)

    def __repr__(self):
        return '<Tip %r>' % self.url

    def as_dict(self):
        """Return a simple ``dict`` representation of this model."""
        return dict((c.name, getattr(self, c.name)) for c in self.__table__.columns)

"""Populate the `publication_date` column.

Revision ID: 17c1af634026
Revises: 3c4c29f0a791
Create Date: 2012-12-13 21:03:03.445346

"""
# revision identifiers, used by Alembic.
revision = '17c1af634026'
down_revision = '3c4c29f0a791'


import html5lib
from dateutil.parser import parse as parse_date


import pytips
from pytips.util import extract_publication_date
from pytips.models import Tip


def _update_tip(tip):
    tip.publication_date = extract_publication_date(tip.rendered_html)


def _erase_publication_date(tip):
    tip.publication_date = None


def upgrade():
    tips = Tip.query.all()
    map(_update_tip, tips)
    pytips.db.session.commit()


def downgrade():
    tips = Tip.query.all()
    map(_erase_publication_date, tips)
    pytips.db.session.commit()

"""Add the `publication_date` column.

Revision ID: 3c4c29f0a791
Revises: 58b68b5e4e3c
Create Date: 2012-11-26 22:28:41.400425

"""

# revision identifiers, used by Alembic.
revision = '3c4c29f0a791'
down_revision = '58b68b5e4e3c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('tip', sa.Column('publication_date', sa.DateTime(timezone=True)))


def downgrade():
    op.drop_column('tip', 'publication_date')


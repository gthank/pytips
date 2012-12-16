"""Make the `publication_date` column required.

Revision ID: 3800f47ba771
Revises: 17c1af634026
Create Date: 2012-12-13 21:14:19.363112

"""

# revision identifiers, used by Alembic.
revision = '3800f47ba771'
down_revision = '17c1af634026'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('tip', 'publication_date', nullable=False)


def downgrade():
    op.alter_column('tip', 'publication_date', nullable=True)

"""Create 'Tip' table.

Revision ID: 58b68b5e4e3c
Revises: None
Create Date: 2012-10-21 18:19:58.413825

"""

# revision identifiers, used by Alembic.
revision = '58b68b5e4e3c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_name', sa.String(), nullable=False),
    sa.Column('author_url', sa.String(length=1024), nullable=False),
    sa.Column('url', sa.String(length=1024), nullable=False),
    sa.Column('rendered_html', sa.String(length=1024), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rendered_html'),
    sa.UniqueConstraint('url')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tip')
    ### end Alembic commands ###

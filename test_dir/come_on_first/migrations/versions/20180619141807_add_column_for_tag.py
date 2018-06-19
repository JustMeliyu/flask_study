"""add column for tag

Revision ID: 763767a279b6
Revises: 
Create Date: 2018-06-19 14:18:07.428395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '763767a279b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('tags', sa.Column('tag_len', sa.Integer))


def downgrade():
    op.drop_column('tags', 'tag_len')

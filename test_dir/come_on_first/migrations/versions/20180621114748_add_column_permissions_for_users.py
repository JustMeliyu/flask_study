"""add column permissions for users

Revision ID: e9b71ae71aa8
Revises: a89a7645b58a
Create Date: 2018-06-21 11:47:48.842196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9b71ae71aa8'
down_revision = '1d90f5992e84'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('permissions', sa.Integer, nullable=False))


def downgrade():
    op.drop_column('users', 'permissions')

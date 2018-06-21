"""add column right for users

Revision ID: a89a7645b58a
Revises: 1d90f5992e84
Create Date: 2018-06-21 10:28:55.993145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a89a7645b58a'
down_revision = '1d90f5992e84'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('right', sa.Integer, nullable=False))


def downgrade():
    op.drop_column("users", "right")

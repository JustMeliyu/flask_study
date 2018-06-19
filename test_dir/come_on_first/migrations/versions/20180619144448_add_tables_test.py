"""add tables test

Revision ID: 8a63803eb402
Revises: 0f5713480f67
Create Date: 2018-06-19 14:44:48.265962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a63803eb402'
down_revision = '0f5713480f67'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True, nullable=False),
        sa.Column('name', sa.String(100))
    )


def downgrade():
    op.drop_table('test')

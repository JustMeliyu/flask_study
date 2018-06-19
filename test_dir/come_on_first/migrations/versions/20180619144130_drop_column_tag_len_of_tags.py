"""drop column tag_len of tags

Revision ID: 0f5713480f67
Revises: 763767a279b6
Create Date: 2018-06-19 14:41:30.546193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f5713480f67'
down_revision = '763767a279b6'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('tags', 'tag_len')


def downgrade():
    op.add_column('tags', sa.Column('tag_len', sa.Integer))

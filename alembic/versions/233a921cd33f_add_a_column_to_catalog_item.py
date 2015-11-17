"""add a column to catalog_item

Revision ID: 233a921cd33f
Revises: 2f5e00995f1d
Create Date: 2015-11-17 11:40:09.726386

"""

# revision identifiers, used by Alembic.
revision = '233a921cd33f'
down_revision = '2f5e00995f1d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('catalog_item', sa.Column('price', sa.Float))


def downgrade():
    op.drop_column('catalog_item', 'price')

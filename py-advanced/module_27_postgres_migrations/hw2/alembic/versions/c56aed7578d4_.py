"""empty message

Revision ID: c56aed7578d4
Revises: 4de6d4f35a6d
Create Date: 2023-03-10 16:43:08.539918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c56aed7578d4'
down_revision = '4de6d4f35a6d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('patronomic', sa.String))


def downgrade() -> None:
    pass

"""user_surname_add

Revision ID: e70c0af944f9
Revises: 50af731aa423
Create Date: 2023-03-10 16:31:11.094278

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e70c0af944f9'
down_revision = '50af731aa423'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('surname', sa.String))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('address', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('coffee_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('has_sale', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['coffee_id'], ['coffee.id'], name='users_coffee_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_table('coffee',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('origin', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('intensifier', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('notes', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='coffee_pkey')
    )
    # ### end Alembic commands ###

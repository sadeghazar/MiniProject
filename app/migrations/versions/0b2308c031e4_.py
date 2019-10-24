"""empty message

Revision ID: 0b2308c031e4
Revises: 58d9b3cf9400
Create Date: 2019-10-24 22:36:59.811978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b2308c031e4'
down_revision = '58d9b3cf9400'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    # ### end Alembic commands ###

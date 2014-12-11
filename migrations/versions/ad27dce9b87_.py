"""empty message

Revision ID: ad27dce9b87
Revises: 2d2603b0d445
Create Date: 2014-11-20 12:56:56.648507

"""

# revision identifiers, used by Alembic.
revision = 'ad27dce9b87'
down_revision = '2d2603b0d445'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'channels', ['name'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'channels')
    ### end Alembic commands ###

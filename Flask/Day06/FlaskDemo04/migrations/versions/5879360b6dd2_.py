"""empty message

Revision ID: 5879360b6dd2
Revises: 
Create Date: 2019-05-27 17:45:47.522858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5879360b6dd2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wife',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wname', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wife')
    # ### end Alembic commands ###

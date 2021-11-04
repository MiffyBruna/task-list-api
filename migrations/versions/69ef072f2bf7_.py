"""empty message

Revision ID: 69ef072f2bf7
Revises: c275089fceb0
Create Date: 2021-10-29 13:26:20.632650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69ef072f2bf7'
down_revision = 'c275089fceb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('title', sa.String(), nullable=True))
    op.add_column('task', sa.Column('description', sa.String(), nullable=True))
    op.add_column('task', sa.Column('completed_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'completed_at')
    op.drop_column('task', 'description')
    op.drop_column('task', 'title')
    # ### end Alembic commands ###

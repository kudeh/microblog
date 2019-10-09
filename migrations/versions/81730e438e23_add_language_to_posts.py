"""add language to posts

Revision ID: 81730e438e23
Revises: e54bbae4b123
Create Date: 2019-10-08 20:40:26.877378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81730e438e23'
down_revision = 'e54bbae4b123'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
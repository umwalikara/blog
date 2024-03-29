"""Initial Migration

Revision ID: c112115a1c8b
Revises: dfe683abc497
Create Date: 2019-09-30 11:34:22.672049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c112115a1c8b'
down_revision = 'dfe683abc497'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('blog', sa.String(), nullable=True))
    op.drop_column('blog', 'content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('blog', 'blog')
    # ### end Alembic commands ###

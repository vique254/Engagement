"""Initial Migration

Revision ID: 442c09d8beeb
Revises: d009a2c61c98
Create Date: 2019-12-05 17:21:55.767235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '442c09d8beeb'
down_revision = 'd009a2c61c98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('parent_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'parent', ['parent_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'parent_id')
    # ### end Alembic commands ###
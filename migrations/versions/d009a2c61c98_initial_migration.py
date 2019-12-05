"""Initial Migration

Revision ID: d009a2c61c98
Revises: 8203372c124d
Create Date: 2019-12-05 17:05:18.926580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd009a2c61c98'
down_revision = '8203372c124d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parent', sa.Column('body', sa.String(length=5000), nullable=True))
    op.add_column('parent', sa.Column('posted_by', sa.String(length=255), nullable=True))
    op.add_column('parent', sa.Column('posted_on', sa.DateTime(), nullable=True))
    op.add_column('parent', sa.Column('title', sa.String(length=255), nullable=True))
    op.add_column('parent', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'parent', 'users', ['user_id'], ['id'])
    op.drop_column('parent', 'parent_title')
    op.drop_column('parent', 'parent_content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parent', sa.Column('parent_content', sa.VARCHAR(length=5000), autoincrement=False, nullable=True))
    op.add_column('parent', sa.Column('parent_title', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'parent', type_='foreignkey')
    op.drop_column('parent', 'user_id')
    op.drop_column('parent', 'title')
    op.drop_column('parent', 'posted_on')
    op.drop_column('parent', 'posted_by')
    op.drop_column('parent', 'body')
    # ### end Alembic commands ###
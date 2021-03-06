"""fish

Revision ID: caa489a6c348
Revises: 3e335dbfd1ac
Create Date: 2017-05-11 09:18:47.634900

"""

# revision identifiers, used by Alembic.
revision = 'caa489a6c348'
down_revision = '3e335dbfd1ac'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fish_record',
    sa.Column('record_id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('image_num', sa.Integer(), nullable=True),
    sa.Column('source', sa.String(length=1000), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('record_id')
    )
    op.create_table('fish_update_info',
    sa.Column('update_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('last_update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('update_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fish_update_info')
    op.drop_table('fish_record')
    # ### end Alembic commands ###

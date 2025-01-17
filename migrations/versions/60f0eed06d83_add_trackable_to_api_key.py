"""add trackable to api key

Revision ID: 60f0eed06d83
Revises: dc61ac1e9b29
Create Date: 2024-10-26 00:37:11.893437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60f0eed06d83'
down_revision = 'dc61ac1e9b29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('api_keys', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('created_by', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_by', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('archived', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('archived_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('archived_by', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('api_keys', schema=None) as batch_op:
        batch_op.drop_column('archived_by')
        batch_op.drop_column('archived_at')
        batch_op.drop_column('archived')
        batch_op.drop_column('updated_by')
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_by')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###

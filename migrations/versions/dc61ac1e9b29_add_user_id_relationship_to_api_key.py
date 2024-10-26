"""add user_id relationship to api key

Revision ID: dc61ac1e9b29
Revises: 0012e0004640
Create Date: 2024-10-26 00:15:36.710280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc61ac1e9b29'
down_revision = '0012e0004640'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('api_keys', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.String(), nullable=False))
        batch_op.create_foreign_key('fk_api_keys_user_id', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('api_keys', schema=None) as batch_op:
        batch_op.drop_constraint('fk_api_keys_user_id', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###

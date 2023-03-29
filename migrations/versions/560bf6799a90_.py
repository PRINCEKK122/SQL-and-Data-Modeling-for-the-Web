"""empty message

Revision ID: 560bf6799a90
Revises: 5c8bd1c81de7
Create Date: 2023-03-29 09:17:40.788459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '560bf6799a90'
down_revision = '5c8bd1c81de7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###

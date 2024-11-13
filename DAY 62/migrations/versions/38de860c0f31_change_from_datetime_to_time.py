"""change from datetime to time

Revision ID: 38de860c0f31
Revises: fd38abf01eb6
Create Date: 2024-02-19 09:55:55.413527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38de860c0f31'
down_revision = 'fd38abf01eb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.alter_column('open_time',
               existing_type=sa.DATETIME(),
               type_=sa.Time(),
               existing_nullable=False)
        batch_op.alter_column('close_time',
               existing_type=sa.DATETIME(),
               type_=sa.Time(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.alter_column('close_time',
               existing_type=sa.Time(),
               type_=sa.DATETIME(),
               existing_nullable=False)
        batch_op.alter_column('open_time',
               existing_type=sa.Time(),
               type_=sa.DATETIME(),
               existing_nullable=False)

    # ### end Alembic commands ###
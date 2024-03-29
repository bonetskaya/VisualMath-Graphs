"""Activity table

Revision ID: 099ea13b0517
Revises: cfd48067fba5
Create Date: 2019-08-29 01:31:10.390324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '099ea13b0517'
down_revision = 'cfd48067fba5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_activity_name'), 'activity', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_activity_name'), table_name='activity')
    op.drop_table('activity')
    # ### end Alembic commands ###

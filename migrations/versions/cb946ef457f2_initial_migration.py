"""Initial migration

Revision ID: cb946ef457f2
Revises: 
Create Date: 2020-06-10 12:58:07.859575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb946ef457f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('country', sa.String(length=2), server_default=sa.text("'RU'"), nullable=False),
    sa.Column('region', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cities_country'), 'cities', ['country'], unique=False)
    op.create_index(op.f('ix_cities_region'), 'cities', ['region'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('id_oauth', sa.String(length=255), nullable=True),
    sa.Column('login', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('status', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    sa.Column('type', sa.Integer(), server_default=sa.text('1'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id_oauth'), 'users', ['id_oauth'], unique=True)
    op.create_index(op.f('ix_users_login'), 'users', ['login'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_login'), table_name='users')
    op.drop_index(op.f('ix_users_id_oauth'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_cities_region'), table_name='cities')
    op.drop_index(op.f('ix_cities_country'), table_name='cities')
    op.drop_table('cities')
    # ### end Alembic commands ###

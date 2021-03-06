"""phones

Revision ID: 2263d61a69c5
Revises: 2a80b10f4fe5
Create Date: 2020-06-17 13:58:24.370552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2263d61a69c5'
down_revision = '2a80b10f4fe5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phones',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('id_city', sa.BigInteger(), nullable=False),
    sa.Column('phone', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('other_phones', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['id_city'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_phones_id_city'), 'phones', ['id_city'], unique=False)
    op.create_index(op.f('ix_phones_phone'), 'phones', ['phone'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_phones_phone'), table_name='phones')
    op.drop_index(op.f('ix_phones_id_city'), table_name='phones')
    op.drop_table('phones')
    # ### end Alembic commands ###

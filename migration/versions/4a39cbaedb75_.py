"""empty message

Revision ID: 4a39cbaedb75
Revises: 624217657b47
Create Date: 2022-10-12 23:22:13.388269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a39cbaedb75'
down_revision = '624217657b47'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ping',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=800), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ping_id'), 'ping', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ping_id'), table_name='ping')
    op.drop_table('ping')
    # ### end Alembic commands ###
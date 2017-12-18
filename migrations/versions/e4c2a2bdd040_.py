"""empty message

Revision ID: e4c2a2bdd040
Revises: 7d38e2e2e7cb
Create Date: 2017-11-20 21:15:07.190000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4c2a2bdd040'
down_revision = '7d38e2e2e7cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tax_rate', sa.Column('hs_code', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tax_rate', 'hs_code')
    # ### end Alembic commands ###

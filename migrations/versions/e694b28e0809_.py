"""empty message

Revision ID: e694b28e0809
Revises: 06e18bdc4682
Create Date: 2017-11-24 02:40:27.307000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e694b28e0809'
down_revision = '06e18bdc4682'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('export_customs_declaration', sa.Column('check_date', sa.Date(), nullable=True))
    op.add_column('import_customs_declaration', sa.Column('check_date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('import_customs_declaration', 'check_date')
    op.drop_column('export_customs_declaration', 'check_date')
    # ### end Alembic commands ###

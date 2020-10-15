"""create test table

Revision ID: 60441eabe3ef
Revises: 
Create Date: 2020-10-15 13:57:02.379881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60441eabe3ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test_table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )

def downgrade():
    op.drop_table('test_table')

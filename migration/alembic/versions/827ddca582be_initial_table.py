"""initial-tables

Revision ID: 827ddca582be
Revises: da1b7b2beaf1
Create Date: 2019-06-06 11:01:11.457213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '827ddca582be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('A',
                    sa.Column('id', sa.Integer, primary_key=True)
                    )

    op.create_table('B',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('category_number', sa.Integer, nullable=False),
                    sa.Column('category_name', sa.String(200), nullable=False)
                    )

    b_seed = sa.sql.table("B",
                            sa.sql.column("category_number", sa.Integer),
                            sa.sql.column("category_name", sa.String)
                            )

    op.bulk_insert(b_seed, [
        {"category_number": "cat1", "category_name": 1},
        {"category_number": "cat2", "category_name": 2},
        {"category_number": "cat3", "category_name": 3},
    ])
                

def downgrade():
    op.drop_table('B')
    op.drop_table('A')

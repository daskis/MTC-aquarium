"""add table rejections for childs 7

Revision ID: b45c138d44db
Revises: ce710530b814
Create Date: 2024-05-18 11:21:50.286702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b45c138d44db'
down_revision: Union[str, None] = 'ce710530b814'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('childrenrejections',
    sa.Column('children_name', sa.String(), nullable=False),
    sa.Column('category_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['category_name'], ['videocategory.name'], ),
    sa.ForeignKeyConstraint(['children_name'], ['childrens.name'], ),
    sa.PrimaryKeyConstraint('children_name', 'category_name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('childrenrejections')
    # ### end Alembic commands ###

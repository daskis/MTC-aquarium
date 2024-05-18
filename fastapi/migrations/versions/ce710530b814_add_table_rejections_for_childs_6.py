"""add table rejections for childs 6

Revision ID: ce710530b814
Revises: 182c68fd2d73
Create Date: 2024-05-18 11:21:04.968121

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce710530b814'
down_revision: Union[str, None] = '182c68fd2d73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('childrenrejections')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('childrenrejections',
    sa.Column('children_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('category_name', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['category_name'], ['videocategory.id'], name='childrenrejections_category_name_fkey'),
    sa.ForeignKeyConstraint(['children_name'], ['childrens.name'], name='childrenrejections_children_name_fkey')
    )
    # ### end Alembic commands ###
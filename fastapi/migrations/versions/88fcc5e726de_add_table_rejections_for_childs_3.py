"""add table rejections for childs 3

Revision ID: 88fcc5e726de
Revises: 10dcc78c2502
Create Date: 2024-05-18 11:09:07.145928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88fcc5e726de'
down_revision: Union[str, None] = '10dcc78c2502'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
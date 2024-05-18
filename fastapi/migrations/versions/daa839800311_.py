"""empty message

Revision ID: daa839800311
Revises: 18cbd19dd559
Create Date: 2024-05-17 23:22:56.492853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'daa839800311'
down_revision: Union[str, None] = '18cbd19dd559'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video_videocategory',
    sa.Column('video_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['videocategory.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['video.id'], ),
    sa.PrimaryKeyConstraint('video_id', 'category_id')
    )
    op.drop_constraint('video_category_id_fkey', 'video', type_='foreignkey')
    op.drop_column('video', 'category_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('video_category_id_fkey', 'video', 'videocategory', ['category_id'], ['id'])
    op.drop_table('video_videocategory')
    # ### end Alembic commands ###
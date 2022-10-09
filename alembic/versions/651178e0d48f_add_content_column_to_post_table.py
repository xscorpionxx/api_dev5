"""add content column to post table

Revision ID: 651178e0d48f
Revises: e46d5acddb4c
Create Date: 2022-10-08 06:21:27.066956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '651178e0d48f'
down_revision = 'e46d5acddb4c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts" , sa.Column("content" , sa.String(200) , nullable = False)) 
    pass


def downgrade() -> None:
    op.drop_column("posts" , 'content')
    pass

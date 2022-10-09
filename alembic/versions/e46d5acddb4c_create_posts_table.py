"""create posts table

Revision ID: e46d5acddb4c
Revises: 
Create Date: 2022-10-08 05:46:52.448597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e46d5acddb4c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() :
    op.create_table("posts" , sa.Column("id" , sa.Integer() , nullable = False , primary_key = True) ,
     sa.Column("title" , sa.String(200) , nullable = False ) )
    pass


def downgrade():
    op.drop_table('posts')
    pass

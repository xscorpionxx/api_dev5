"""add forign key for post

Revision ID: 4c5cd52005ee
Revises: dda3a7e14732
Create Date: 2022-10-08 06:38:44.123068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c5cd52005ee'
down_revision = 'dda3a7e14732'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts' , sa.Column("owner_id" , sa.Integer() , nullable = False))
    op.create_foreign_key('posts_users_fk' , source_table="posts" , referent_table="users"
    , local_cols=['owner_id'] , remote_cols=['id'] , ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint("posts_users_fk",table_name="posts")
    op.drop_column("posts" , 'owner_id')
    pass

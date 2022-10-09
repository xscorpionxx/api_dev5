"""Add user table

Revision ID: dda3a7e14732
Revises: 651178e0d48f
Create Date: 2022-10-08 06:28:45.952582

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null ,text

# revision identifiers, used by Alembic.
revision = 'dda3a7e14732'
down_revision = '651178e0d48f'
branch_labels = None
depends_on = None


def upgrade() :
    op.create_table("users" ,
     sa.Column("id" , sa.Integer() , nullable = False ) ,
     sa.Column("email" , sa.String(200) , nullable = False )
     ,sa.Column("name" , sa.String(200) , nullable = False )
     ,sa.Column("password" , sa.String(200) , nullable = False )
     ,sa.Column("created_at" , sa.TIMESTAMP(timezone=True) ,server_default = text('current_timestamp'), nullable = False )
     ,sa.PrimaryKeyConstraint('id'),
     sa.UniqueConstraint('email') )
   
    pass


def downgrade():
    op.drop_table("users")
    pass

from pymysql import Timestamp
from .database import Base
from sqlalchemy import Column, ForeignKey , Integer ,String , TIMESTAMP
from sqlalchemy.sql.expression import null ,text
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship

class Posts(Base) : 
    __tablename__ = "posts"

    id = Column(Integer , primary_key = True , nullable = False )
    title = Column(String(200) , nullable = False , )
    content = Column(String(200) , nullable = False)
    created_at = Column(TIMESTAMP(timezone=True) , nullable = False , server_default = text('current_timestamp') ,
    )
    # for forign key
    owner_id = Column(Integer , ForeignKey("users.id" , ondelete="CASCADE") , nullable = False)

    #### to get all data from another table using relationship but dont forget to update the schema 
    user = relationship("User")

class User(Base) : 
    __tablename__ = "users"

    id = Column(Integer , primary_key = True , nullable = False )
    name = Column(String(200) , nullable = False , )
    password = Column(String(200) , nullable = False)
    email = Column(String(200) , nullable = False , unique = True)
    created_at = Column(TIMESTAMP(timezone=True) , nullable = False , server_default = text('current_timestamp') ,
    )
    UniqueConstraint("email")
    
#### to make column to default add server_default tp true
class Vote(Base) : 
    __tablename__ = "votes"
    user_id = Column(Integer , ForeignKey("users.id",ondelete="CASCADE") ,primary_key = True)
    post_id = Column(Integer , ForeignKey("posts.id",ondelete="CASCADE") ,primary_key = True)
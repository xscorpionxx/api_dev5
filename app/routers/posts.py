from typing import List, Optional
from fastapi import  Depends, Response , status , HTTPException  ,APIRouter
from sqlalchemy.orm import Session

from sqlalchemy import func
from .. import oauth2
from ..models import User , Posts ,Vote
from .utils import hash_
from ..database import get_db

from datetime import datetime
from pydantic import BaseModel, PathNotExistsError

router = APIRouter(tags= ["posts"])

class post_info(BaseModel) : 
    title  : str
    content : str


class user_info(BaseModel) : 
    name  : str
    password : str
    email : str  
class createuser_res(user_info) : 
    created_at : datetime
    id : int
    class Config : 
        orm_mode = True


class createpost_res(post_info) : 
    created_at : datetime
    id : int
    user_id : int
    user : createuser_res
    class Config : 
        orm_mode = True

class createpostwithvotes_res(BaseModel) :
    Posts : createpost_res
    votes : int
    class Config : 
        orm_mode = True


@router.post('/create_post' ,status_code= status.HTTP_201_CREATED ,response_model= createpost_res 
 )
def createpost(post : post_info ,db : Session = Depends(get_db),user_id_ : int = Depends(oauth2.get_current_user) 
):
    new_post = post.dict()
    new_post =  Posts(user_id =user_id_.id ,**new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post


@router.get("/posts" , response_model= List[createpostwithvotes_res]
) 
def getposts(db : Session = Depends(get_db) ,user_id_ : int = Depends(oauth2.get_current_user)
,limit : int =10 , skip :int =0 , search : Optional[str] ="") : 

    posts = db.query(Posts).filter(Posts.title.contains(search)).limit(limit).offset(skip).all()
    
    posts_with_votes = db.query(Posts , func.count(Vote.post_id).label("votes")
    ).join(Vote , Vote.post_id == Posts.id , isouter = True).group_by(Posts.id).filter(Posts.title.contains(search)).limit(limit).offset(skip).all()
    
    
    return  posts_with_votes

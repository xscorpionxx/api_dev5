from typing import List
from fastapi import  Depends, Response , status , HTTPException  ,APIRouter
from sqlalchemy.orm import Session

from .. import oauth2
from ..models import User , Vote , Posts
from .. import schema
from .utils import hash_
from ..database import get_db
from pydantic import BaseModel, conint

from .. import database
### schema
#### dir should 1 or 0
class vote(BaseModel):
    post_id : int
    dir : conint(le = 1)


router = APIRouter(tags= ["votes"] , prefix="/vote")

@router.post("/" , status_code=status.HTTP_201_CREATED)
def vote(vote_ : vote , db : Session = Depends(database.get_db) , current_user : int = Depends(oauth2.get_current_user)):
    posts = db.query(Posts).filter(Posts.id == vote_.post_id ).first()
    if not posts : 
        raise HTTPException(detail="post not fount " , status_code= status.HTTP_404_NOT_FOUND)
    vote_query =  db.query(Vote).filter(Vote.post_id == vote_.post_id , Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if (vote_.dir == 1) :
        if found_vote : 
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="voted before")
        new_vote = Vote(post_id = vote_.post_id , user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message" : "done"}
    
    else : 
        if not found_vote : 
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="not voted before")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message" : "sucessfuly_deleted"}


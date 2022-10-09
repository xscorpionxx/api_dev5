
from fastapi import APIRouter  ,Depends , HTTPException ,status , Response
from ..schema import user_login
from sqlalchemy.orm import Session
from..database import get_db
from ..models import User
from fastapi.security.oauth2 import  OAuth2PasswordRequestForm
from .utils import verify
from .. import oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user : OAuth2PasswordRequestForm = Depends() ,db : Session= Depends(get_db) ):
    #### this will convert email key to username
    ##### so 
    #user_ =  db.query(User).filter(User.email == user.email).first()
    ### so username = email
    # ### and we will send it in from-data not row 
    user_ =  db.query(User).filter(User.email == user.username).first()
    if not user_  : 
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN ,
        detail=f"invalid creds")

    if not  verify(user.password  ,user_.password) : 
            raise HTTPException(status_code= status.HTTP_403_FORBIDDEN ,
             detail=f"invalid creds")
    
    ######## we need to create token 
    ##### you can input what you want info 
    access_token = oauth2.create_access_tokeen(data= {"user_id": user_.id})
    return {"token" : access_token  ,"token_type" : "barrer"}

    
    


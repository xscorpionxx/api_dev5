from tkinter import E
from typing import Optional
from pydantic import BaseModel
from fastapi import Depends ,status , HTTPException
from jose import JWTError , jwt 
from datetime import datetime , timedelta
#### SECRET KEY  
#### algorithm 
# expiration time
from fastapi.security import OAuth2PasswordBearer 
from .config import settings


class TokenData(BaseModel) : 
    id : Optional[str] = None
oauth2_scheme = OAuth2PasswordBearer(tokenUrl= 'login')

SECRET_KEY =  settings.secret_key

ALGORITHM = settings.algorithm

ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expired 


def create_access_tokeen(data : dict) :
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})

    encoded = jwt.encode(to_encode , SECRET_KEY ,algorithm= ALGORITHM)
    return encoded


def verify_access_token(token : str , credential_exception) :
    try  :
        payload = jwt.decode(token , SECRET_KEY ,  algorithms= [ALGORITHM])

        id : str =  payload.get("user_id")
        if id is None : 
            raise credential_exception
        token_Data = TokenData(id=id)
    except JWTError : 
        raise credential_exception

    return token_Data

def get_current_user(token : str = Depends(oauth2_scheme)) : 
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , detail = "not validate cred" ,
    headers = {"WWW-Authenticate" : "Bearer"})
    return verify_access_token(token , credentials_exception) 

###### we will resturct this schemas

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class user_info(BaseModel) : 
    name  : str
    email : str
    password : str
    #published : Optional[bool] =True
    # this mean if published not given in post
    # then it will be True as default
    #rating : Optional[int] = None
    # this is optional value 

class createuser(user_info) : 
    pass

### for example we need user just to update name so
# we drop othe columns
class updateuser(user_info) : 
    pass


     
#### for response 
class createuser_res(user_info) : 
    status :bool =  True
    created_at : datetime
    id : int
    class Config : 
        orm_mode = True


class post_info(BaseModel) : 
    title  : str
    content : str
    

class createpost_res(post_info) : 
    created_at : datetime
    id : int
    user_id : int
    class Config : 
        orm_mode = True

class user_login(BaseModel) : 
    password : str
    email : str
class Token(BaseModel) : 
    access_token : str
    token_type : str

class TokenData(BaseModel) : 
    id : Optional[str] = None

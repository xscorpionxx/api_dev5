from fastapi import  FastAPI , Depends
from pydantic import BaseSettings
from sqlalchemy.orm import Session
from . import models
from fastapi.middleware.cors import CORSMiddleware
from .database import engine ,get_db
from .config import settings
from .routers import users , auth , posts , votes
####### WE WANT TO SAVE IT 

#####models.Base.metadata.create_all(bind= engine)

app = FastAPI()

app.add_middleware(
CORSMiddleware ,
allow_origins =[
"https://www.google.com"
] ,
allow_credentials=True ,
allow_methods =["*"] ,
allow_headers =["*"]
)

# @app.get("/sqlalchemy")
# def test_users(db : Session = Depends(get_db)):
#     users =  db.query(models.User).all()
#     return {"data" : users}

########### get
@app.get('/')
def get_user() : 
    return {"msg" : "hello___"}

##### to get all routers
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(votes.router)
######## pos

# @app.post('/login_')
# def login(payload : dict = Body(...)):
#     name = None
#     password = None

#     return {"name" : name ,
#         "password" : password } 
# payload : body mean that we will get the data
# FROM REQUEST
### but we need schema to force the user to
# sent what we need so we will tell the user what format we want 
#  so we will use pydantic

# we need name : str and content : str , email : str




#@app.post('/loginA')
#def login(userinfo_ : createuser):
#    userdict = userinfo_.dict()
#    userdict['id'] = random.randrange(0,10000)
#    my_users.append(userdict)
#    return  {"Data"  : userdict}
#@app.get("/users") 
#def getusers() : 
#    return {"data" : my_users}
############ waht is crud it means 
### c is creat so post but r mean read so get 
# u is update so put or patch ,d is delete so delte
#you can add params is get method in url so for 
#  example we need id in update and delete and 
# read specific thing 
##### you should order your func because 
# when we have request it start from top to
# bottom so  if there are tow func that 
# similr by routes it will through an error


#######



from typing import List
from fastapi import  Depends, Response , status , HTTPException  ,APIRouter
from sqlalchemy.orm import Session

from .. import oauth2
from ..models import User
from .. import schema
from .utils import hash_
from ..database import get_db

router = APIRouter(tags= ["Users"])

# this is for to not to re write same prefix
# router = APIRouter(
#     prefix="/users"
# )
@router.get("/users/{id}")
def get_user(id : int ,db : Session = Depends(get_db) ,user_id : int = Depends(oauth2.get_current_user) ) : 
    # global cursor , conn
    
    # cursor.execute(f"""SELECT * FROM USERS where id = {id} """ )
    # user = cursor.fetchall()
    
    # if  len(user) == 0 : 
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
    #         detail= f"user with id = {id} not found")
    print(user_id)
    user = db.query(User).filter(User.id == id).first()
    if  not user : 
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
             detail= f"user with id = {id} not found")
    return   user



## we should resturct the response so it 
# will be obvius to the user using http status code
### or we can user raise http exception
#### you can change default status code 
## in the decorator like below
@router.post('/signin' ,status_code= status.HTTP_201_CREATED ,response_model= schema.createuser_res 
)
def createuser(user : schema.user_info ,db : Session = Depends(get_db)):
    # global cursor ,conn
    # try : 
    #     pro = cursor.execute("""INSERT INTO USERS (Name , password , email) values (%s , %s , %s) """,
    #     (userinfo_.name , userinfo_.email , userinfo_.password ))
    #     if pro ==1 :
    #        conn.commit() 
    # except Exception as e : 
    #     return e.args 


    #### hash the password
    print(user)
    hashed_pass = hash_(user.password)
    user.password = hashed_pass
    new_user =  User(**user.dict())
    exists = db.query(User).filter(new_user.email == User.email).first() 
    if exists !=None : 
            raise HTTPException(status_code=status.HTTP_302_FOUND , 
            detail= f"user with email = {new_user.email} is existed")
    
    db.add(new_user)
    
    db.commit()
    db.refresh(new_user)
    return    new_user 



@router.get("/users" , response_model= List[schema.createuser_res]) 
def getusers(db : Session = Depends(get_db) ) : 
    #global cursor , conn
    #try : 
    #    cursor.execute("""SELECT * FROM USERS """ )
    #    data = cursor.fetchall()
    #    print(data)
    #except Exception as e : 
     #   print(e.args)
     #   return e.args
    users = db.query(User).all()
    return   users



#######333 to delete
@router.delete('/users/{id}' ,status_code= status.HTTP_204_NO_CONTENT)
def delete(id,db : Session = Depends(get_db)) : 
    # global conn , cursor
    # deleted_user = cursor.execute("""delete from users where id = %s """,
    #     (id))
    # conn.commit()  
    deleted_user = db.query(User).filter(User.id == id)
    if deleted_user.first() == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
        detail= f"user with id = {id} not found")

    else : 
        deleted_user.delete(synchronize_session=False)
        db.commit()
    return Response(status_code= status.HTTP_204_NO_CONTENT)


#####update
@router.put("/users/{id}")
def update_user(id : int , userinfo : schema.updateuser ,db : Session = Depends(get_db)) : 
    # global conn , cursor
    # updated_user = cursor.execute("""update users set Name = %s , email = %s , password = %s where id = %s """ ,
    # (userinfo.name , userinfo.email , userinfo.password ,id))
    # conn.commit()
    user_ =  db.query(User).filter(User.id == id )
    updated_user = user_.first()
    if updated_user == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
        detail= f"user with id = {id} not found")
    user_.update(userinfo.dict() ,
    synchronize_session=False)
    db.commit()
    return user_.first()
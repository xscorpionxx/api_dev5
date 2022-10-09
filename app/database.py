######## orm
#####
from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
#SQLALCHEMY_DATABASE_URL = 'mysql://<username>:<password>@<ip-address/hostname>/<databse_name>'
SQLALCHEMY_DATABASE_URL = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(settings.database_username, settings.database_password ,settings.database_hostname, settings.database_port,settings.database_name)
#SQLALCHEMY_DATABASE_URL = 'mysql://{0}:{1}@{2}:{3}/{4}'.format("root", "almuazen2001" ,"localhost"  ,8888,"training_data")
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#### session
sessionlocal = sessionmaker(autocommit=False , 
autoflush= False , bind = engine)

Base = declarative_base()

def get_db():
    db = sessionlocal()
    try : 
        yield db
    finally : 
        db.close()

# def  connect_with_database(hosturl = 'localhost' , tport = int(8888), tuser= 'root' , password = 'almuazen2001'
#                          ,dbt = 'training_data'):
#     while True : 
#         global conn
#         global cursor
#         try : 
#             conn=pymysql.connect(host=hosturl,port=tport
#                                         ,user=tuser,
#                                         passwd=password,
#                                         db=dbt)
#             cursor = conn.cursor()
#             print("connected to database")
#             break
#         except Exception as e : 
#             time.sleep(2)
#             print(e.args)

# #connect_with_database()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2 # main server > postgres 
import time # conn - reloading                                     
from psycopg2.extras import RealDictCursor
from .config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:78865795@localhost/fastapi" (old_login)

#new.env file access > config > env
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 

# # conn = database > sqlalchemy > postgres > old_method

# while True: veroxgeq

#     try:                                           
#         conn = psycopg2.connect(host="localhost", database='fastapi', user='postgres', 
#         password='78865795', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(5)

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},  
#             {"title": "favorite food", "content": "i like pizza", "id": 2}]

# # logic method

# def find_post(id):
#     for p in my_posts:
#         if p ["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p ['id'] == id:
#             return i
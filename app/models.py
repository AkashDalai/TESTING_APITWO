from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, text, true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column (String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
    #rel > posts > user_id
    owner_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"), nullable=False)  
    
    #fatch_user based on post_id > user/post_info > one_group relation
    owner = relationship("User")

class User(Base): # no error
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True) # unique cons = one type
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
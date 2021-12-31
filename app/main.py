from fastapi import FastAPI                                                             
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware # localhost > openweb 

# models.Base.metadata.create_all(bind=engine) # the sqlalchemy update to postgres

app = FastAPI()

#depl > web > 111948 > CORS (Cross-Origin Resource Sharing)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# route - pass > post, user 
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# Inst > method
@app.get("/")
def root():
    
    return {"message": "Let's Say Hi"}
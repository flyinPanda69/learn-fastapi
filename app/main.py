from typing import List, Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from sqlalchemy.orm import Session

from app.utils import get_hash_string

from . import models
from .database import engine, get_db
from .schemas import PostBase,PostCreate, Post, UserCreate, UserOut
from .routers import posts, users, auth



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='admin123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was successfull!')
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(5)



app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get('/')
async def root():
    return {"message": "Hello World"}

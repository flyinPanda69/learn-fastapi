from pydantic import BaseModel, EmailStr
from datetime import datetime

# to create a new post we need the following for now
# title str, content str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime

    #This will help to the sqlalchemy object to be directly converted to pydantic class type
    class Config:
        from_attributes = True
 
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    #This will help to the sqlalchemy object to be directly converted to pydantic class type
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str
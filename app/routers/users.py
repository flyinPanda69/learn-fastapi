from fastapi import  status, HTTPException, Depends, APIRouter
import time

from sqlalchemy.orm import Session

from app.utils import get_hash_string

from app import models
from app.database import get_db
from app.schemas import UserCreate, UserOut


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):


    #hash the password - user.password
    hash_password = get_hash_string(user.password)
    user.password = hash_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)

    return new_user


@router.get("/{id}", response_model= UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} was not found")
    
    return user
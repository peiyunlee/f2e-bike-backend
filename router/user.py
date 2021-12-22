from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.schemas import UserRequestSchema, UserResponseSchema
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)


@router.post('', response_model=UserResponseSchema)
def register(request: UserRequestSchema, db: Session = Depends(get_db)):
    return db_user.register(db=db, request=request)


@router.get('/all', response_model=List[UserResponseSchema])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


@router.get('/email/{user_email}', response_model=UserResponseSchema)
def get_user_by_email(user_email: str, db: Session = Depends(get_db)):
    return db_user.get_user_by_email(user_email=user_email, db=db)


@router.get('/id/{user_id}', response_model=UserResponseSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(user_id=user_id, db=db)

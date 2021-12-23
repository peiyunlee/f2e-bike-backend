from fastapi import HTTPException, status
from router.schemas import UserRequestSchema
from sqlalchemy.orm.session import Session
from sqlalchemy import func
from db.models import DbUser, DbStore
from typing import List


def register(db: Session, request: UserRequestSchema) -> DbUser:
    users = db.query(DbUser).filter(DbUser.email == request.email).first()
    if users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Email already registered')

    new_user = DbUser(
        email=request.email,
        password=request.password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session) -> List[DbUser]:
    users = db.query(DbUser).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Users not found')
    return users


def get_user_by_id(user_id: int, db: Session) -> DbUser:
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id) = {user_id} not found')
    return user


def get_user_by_email(user_email: str, db: Session) -> DbUser:
    user = db.query(DbUser).filter(func.upper(
        DbUser.email) == user_email.upper()).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with email = {user_email} not found')
    return user

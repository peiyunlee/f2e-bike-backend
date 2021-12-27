from typing import List
from fastapi import HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from sqlalchemy import func, exc
from sqlalchemy.exc import IntegrityError

from router.schemas import StoreRequestSchema
from db.models import DbStore
from .db_user import create_access_token


def create(db: Session, request: StoreRequestSchema):
    store = db.query(DbStore).filter(DbStore.user_id == request.user_id).first()
    
    if store:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Store with userid = {request.user_id} already exist')
    
    new_store = DbStore(
        user_id=request.user_id,
        username=request.username,
    )

    db.add(new_store)
    db.commit()

    return {
        'store_id':new_store.id,
        'user_id': new_store.user_id,
        'route_items': []
    }


def get_all_store(db: Session) -> List[DbStore]:
    stores = db.query(DbStore).all()
    if not stores:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Stores not found')
    return stores


def get_store_by_user_id(user_id: int, db: Session) -> DbStore:
    store = db.query(DbStore).filter(DbStore.user_id == user_id).first()
    if not store:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Store with userId = {user_id} not found')

    return store



from fastapi import HTTPException, status
from router.schemas import StoreRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbStore
from typing import List


def create(db: Session, request: StoreRequestSchema):
    new_store = DbStore(
        user_id=request.user_id,
        username=request.username,
    )

    db.add(new_store)
    db.commit()

    return {
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


def get_store_routes_by_user_id(user_id: int, db: Session) -> DbStore:
    store = db.query(DbStore).filter(DbStore.user_id == user_id).first()
    if not store:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Store with userId = {user_id} not found')
    routes = store.route_items
    return store

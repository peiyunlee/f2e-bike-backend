from hashlib import new
from fastapi import HTTPException, status
from router.schemas import RouteRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbRouteItem, DbStore
from typing import List
from .db_user import create_access_token


def store_route(db: Session, request: RouteRequestSchema) -> DbRouteItem:

    store = db.query(DbStore).filter(DbStore.id == request.store_id).first()

    if not store:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Store not create')

    new_route = DbRouteItem(
        store_id=request.store_id,
        city=request.city,
        routename=request.routename,
    )

    db.add(new_route)
    db.commit()

    access_token = create_access_token(data={'username': store.username})

    return {
        'access_token': access_token,
        'store_id': new_route.id,
        'city': new_route.city,
        'routename': new_route.routename
    }


def remove_store_route(db: Session, request: RouteRequestSchema) -> DbRouteItem:

    route = db.query(DbRouteItem).filter(DbRouteItem.store_id == request.store_id and DbRouteItem.city ==
                                         request.city and DbRouteItem.routename == request.routename).first()

    if not route:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Route not find')

    db.delete(route)
    db.commit()

    return {
        'store_id': route.store_id,
        'city': route.city,
        'routename': route.routename
    }


def get_store_routes_by_user_id(user_id: int, db: Session) -> List[DbRouteItem]:
    store = db.query(DbStore).filter(DbStore.user_id == user_id).first()
    if not store:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Store with userId = {user_id} not found')
    return store

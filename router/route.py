from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.schemas import RouteRequestSchema,RouteResponseSchema
from router.schemas import StoreResponseWithRouteSchema
from db.database import get_db
from db import db_route,db_store

router = APIRouter(
    prefix='/api/v1/store/route',
    tags=['store_route']
)


@router.post('', response_model = RouteResponseSchema)
def store_route(request: RouteRequestSchema, db: Session = Depends(get_db)):
    return db_route.store_route(db, request)


@router.get('/user/{user_id}', response_model=StoreResponseWithRouteSchema)
def get_store_routes_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return db_store.get_store_routes_by_user_id(user_id=user_id, db=db)
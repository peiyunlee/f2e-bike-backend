from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.schemas import RouteRequestSchema, UserRequestSchema
from router.schemas import StoreResponseWithRouteSchema
from db.database import get_db
from db import db_route
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix='/api/v1/store/route',
    tags=['store_route']
)


@router.post('')
def store_route(request: RouteRequestSchema, db: Session = Depends(get_db), current_user: UserRequestSchema = Depends(get_current_user)):
    return db_route.store_route(db, request)


@router.post('/remove')
def remove_store_route(request: RouteRequestSchema, db: Session = Depends(get_db), current_user: UserRequestSchema = Depends(get_current_user)):
    return db_route.remove_store_route(db, request)


@router.get('/user/{user_id}', response_model=StoreResponseWithRouteSchema)
def get_store_routes_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return db_route.get_store_routes_by_user_id(user_id=user_id, db=db)

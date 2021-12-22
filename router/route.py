from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.schemas import RouteRequestSchema,RouteResponseSchema
from db.database import get_db
from db import db_route
from typing import List

router = APIRouter(
    prefix='/api/v1/store',
    tags=['store_route']
)


@router.post('', response_model = RouteResponseSchema)
def store_route(request: RouteRequestSchema, db: Session = Depends(get_db)):
    return db_route.store_route(db, request)


@router.get('/all', response_model=List[RouteResponseSchema])
def get_all_store(db: Session = Depends(get_db)):
    return db_route.get_all_store(db)

@router.get('/user/{user_id}', response_model=List[RouteResponseSchema])
def get_all_store_by_user_id(user_id: int,db: Session = Depends(get_db)):
    return db_route.get_all_store_by_user_id(user_id,db)
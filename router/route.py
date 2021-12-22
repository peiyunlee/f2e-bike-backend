from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.schemas import RouteRequestSchema,RouteResponseSchema
from db.database import get_db
from db import db_route

router = APIRouter(
    prefix='/api/v1/store/route',
    tags=['store_route']
)


@router.post('', response_model = RouteResponseSchema)
def store_route(request: RouteRequestSchema, db: Session = Depends(get_db)):
    return db_route.store_route(db, request)
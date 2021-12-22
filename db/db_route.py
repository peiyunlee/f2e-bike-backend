from fastapi import HTTPException, status
from router.schemas import RouteRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbRoute
from typing import List


def store_route(db: Session, request: RouteRequestSchema) -> DbRoute:
    new_route = DbRoute(
        city=request.city,
        cycling_length=request.cycling_length,
        routename=request.routename,
        roadsection_start=request.roadsection_start,
        roadsection_end=request.roadsection_end,
        positions=request.positions,
        user_id=request.user_id,
    )
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route


def get_all_store(db: Session) -> List[DbRoute]:
    return db.query(DbRoute).all()


def get_all_store_by_user_id(user_id: int, db: Session) -> List[DbRoute]:
    return db.query(DbRoute).filter(DbRoute.user_id == user_id).all()

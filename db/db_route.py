from fastapi import HTTPException, status
from router.schemas import RouteRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbRouteItem, DbStore

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

    return new_route


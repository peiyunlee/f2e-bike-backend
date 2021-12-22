from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.schema import ForeignKey


class DbRouteItem(Base):
    __tablename__ = 'route_item'
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey('store.id'))
    city = Column(String, nullable=False)
    routename = Column(String, nullable=False)
    

class DbStore(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    route_items = relationship('DbRouteItem')


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey

class DbRouteItem(Base):
    __tablename__ = 'route_item'
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(10), nullable=False)
    routename = Column(String(100), nullable=False)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)

class DbStore(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    username = Column(String(30), ForeignKey('user.username'), nullable=False)
    route_items = relationship('DbRouteItem')
    # station_items = relationship('DbStationItem')

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

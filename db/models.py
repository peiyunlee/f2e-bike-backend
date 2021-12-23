from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey


# class DbStationItem(Base):
#     __tablename__ = 'station_item'
#     id = Column(Integer, primary_key=True, index=True)
#     store_id = Column(Integer, ForeignKey('store.id'))
#     city = Column(String, nullable=False)
#     station_UID = Column(Integer, nullable=False)


class DbRouteItem(Base):
    __tablename__ = 'route_item'
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    routename = Column(String, nullable=False)
    store_id = Column(Integer, ForeignKey('store.id'))

class DbStore(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    username = Column(Integer, ForeignKey('user.username'))
    route_items = relationship('DbRouteItem')
    # station_items = relationship('DbStationItem')

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

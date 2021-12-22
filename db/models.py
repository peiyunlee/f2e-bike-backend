from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.schema import ForeignKey


class DbRoute(Base):
    __tablename__ = 'route'
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    cycling_length = Column(Integer, nullable=False)
    routename = Column(String, nullable=False)
    roadsection_end = Column(String, nullable=False)
    roadsection_start = Column(String, nullable=False)
    positions = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./bike.db"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:111034016@localhost:3306/bike"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
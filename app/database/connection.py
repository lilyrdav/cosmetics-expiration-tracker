from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from fastapi import Depends
from sqlalchemy.orm import Session

DATABASE_URL = os.getenv(
  "DATABASE_URL",
  "postgresql://lily.davoren@localhost:5432/cosmetics_db"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine
)

Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
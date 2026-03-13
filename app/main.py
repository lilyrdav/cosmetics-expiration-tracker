from fastapi import FastAPI
from app.database.connection import engine, Base
from app.routers import users

app = FastAPI(
  title = "Cosmetics Expiration Tracker API",
  version = "0.1.0")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)


@app.get("/")
def read_root():
  return {"message": "Cosmetics Expiration Tracker API is running"}

@app.get("/health")
def health_check():
  return {"status": "healthy"}

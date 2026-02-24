from fastapi import FastAPI

app = FastAPI(
  title = "Cosmetics Expiration Tracker API",
  version = "0.1.0")

@app.get("/")
def read_root():
  return {"message": "Cosmetics Expiration Tracker API is running"}

@app.get("/health")
def health_check():
  return {"status": "healthy"}
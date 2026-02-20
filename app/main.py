from fastapi import FastAPI

app = FastAPI(title = "Cosmetics Expiration Tracker API")

@app.get("/")
def read_root():
  return {"message": "Cosmetics Expiration Tracker API is running"}
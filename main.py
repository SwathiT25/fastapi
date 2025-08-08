from fastapi import FastAPI  # <-- This line is required!

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
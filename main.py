from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


class User(BaseModel):
    name: str

@app.post("/greet")
def greet_user(user: User):
    return {"message": f"Hello, {user.name}!"}


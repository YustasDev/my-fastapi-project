from fastapi import FastAPI
from pydantic import BaseModel
from exceptions import validation_exception_handler  # Импортируем обработчик ошибок
from fastapi.exceptions import RequestValidationError
app = FastAPI()

# Регистрация обработчика ошибок
app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


class User(BaseModel):
    name: str

@app.post("/greet")
def greet_user(user: User):
    return {"message": f"Hello, {user.name}!"}


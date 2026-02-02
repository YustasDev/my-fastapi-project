from dotenv import load_dotenv
from fastapi.exceptions import RequestValidationError
from exceptions import validation_exception_handler

load_dotenv()

from fastapi import FastAPI
from users import router as users_router
from posts import router as posts_router

# Если вам нужно создать таблицы при старте, импортируйте engine и Base из database
from database import engine, Base

# Base.metadata.create_all(bind=engine) # Раскомментируйте, если нужно создавать таблицы

app = FastAPI()

app.add_exception_handler(RequestValidationError, validation_exception_handler)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(users_router)
app.include_router(posts_router)
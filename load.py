
from fastapi import FastAPI
from users import router as users_router
# Если вам нужно создать таблицы при старте, импортируйте engine и Base из database
from database import engine, Base

# Base.metadata.create_all(bind=engine) # Раскомментируйте, если нужно создавать таблицы

app = FastAPI()

app.include_router(users_router)
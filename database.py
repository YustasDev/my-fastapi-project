# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# ================= synchronous connection to the database =====================>
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
# ==============================================================================<

# ================ asynchronous connection to the database ======================

# Асинхронное подключение к базе данных
engine = create_async_engine(DATABASE_URL, echo=True)

# Сессия для асинхронной работы
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


# Функция для получения сессии базы данных
async def get_db():
    async with SessionLocal() as db:
        yield db


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
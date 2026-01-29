from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserResponse
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.future import select
from typing import List


router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@router.get("/users/", response_model=List[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.name = user.name
    db_user.email = user.email
    await db.commit()
    await db.refresh(db_user)
    return db_user


# синхронный контроллер
# @router.post("/users/", response_model=UserResponse)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(name=user.name, email=user.email)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @router.get("/users/{user_id}", response_model=UserResponse)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     return db_user
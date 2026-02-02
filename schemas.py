from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        # orm_mode = True
        from_attributes = True  # for Pydantic V2

class Token(BaseModel):
    access_token: str
    token_type: str


# Схема для создания нового поста
class PostCreate(BaseModel):
    title: str
    content: str
    owner_id: int

# Схема для ответа по посту (с добавленными полями, например, ID и временем создания)
class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int

    class Config:
        orm_mode = True  # позволяет Pydantic работать с SQLAlchemy моделями


# Схема для создания нового комментария
class CommentCreate(BaseModel):
    content: str
    post_id: int
    owner_id: int

# Схема для ответа по комментарию
class CommentResponse(BaseModel):
    id: int
    content: str
    post_id: int
    owner_id: int

    class Config:
        orm_mode = True  # позволяет Pydantic работать с SQLAlchemy моделями


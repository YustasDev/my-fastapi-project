from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Post, Comment
from schemas import PostCreate, PostResponse, CommentCreate, CommentResponse
from database import get_db

router = APIRouter()

# Создание поста
@router.post("/posts/", response_model=PostResponse)
async def create_post(post: PostCreate, db: AsyncSession = Depends(get_db)):
    db_post = Post(title=post.title, content=post.content, owner_id=post.owner_id)
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post

# Получение поста по ID
@router.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Post).filter(Post.id == post_id))
    db_post = result.scalars().first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

# Добавление комментария
@router.post("/comments/", response_model=CommentResponse)
async def create_comment(comment: CommentCreate, db: AsyncSession = Depends(get_db)):
    db_comment = Comment(content=comment.content, post_id=comment.post_id, owner_id=comment.owner_id)
    db.add(db_comment)
    await db.commit()
    await db.refresh(db_comment)
    return db_comment


import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from models import User
from config import DATABASE_URL

async def simulate_login(username):
    engine = create_async_engine(DATABASE_URL)
    async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    
    async with async_session() as db:
        print(f"Querying for email: '{username}'")
        result = await db.execute(select(User).filter(User.email == username))
        db_user = result.scalars().first()
        if db_user:
            print(f"Found user: {db_user.email}, id={db_user.id}")
        else:
            print("User NOT found (None)")
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(simulate_login("vl@example.com"))

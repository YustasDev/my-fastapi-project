import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select
from models import User
from config import DATABASE_URL

async def check():
    engine = create_async_engine(DATABASE_URL)
    async with engine.connect() as conn:
        res = await conn.execute(select(User))
        for u in res:
            print(f"USER: id={u.id} email={repr(u.email)}")
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(check())

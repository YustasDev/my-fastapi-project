import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select
from models import User
from config import DATABASE_URL

async def check_users():
    try:
        engine = create_async_engine(DATABASE_URL)
        async with engine.connect() as conn:
            result = await conn.execute(select(User))
            users = result.fetchall()
            print(f"Total users found: {len(users)}")
            for user in users:
                print(f"User: id={user.id}, name={user.name}, email={user.email}")
        await engine.dispose()
    except Exception as e:
        print(f"Error checking users: {e}")

if __name__ == "__main__":
    asyncio.run(check_users())

# app/db/session.py
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings

# ১. ডাটাবেসের সাথে অ্যাসিনক্রোনাস ইঞ্জিন কানেক্ট করা
engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
)

# ২. সেশন তৈরির কারখানা (Session Factory)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# ৩. প্রতি রিকোয়েস্টে সেশন দেওয়ার জেনারেটর ফাংশন
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
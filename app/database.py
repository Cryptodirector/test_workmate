import os

from dotenv import load_dotenv, find_dotenv
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

load_dotenv(find_dotenv())

MODE = os.getenv('MODE')


DATABASE_URL = settings.database_url

engine = create_async_engine(DATABASE_URL)


DATABASE_URL = settings.database_url


async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

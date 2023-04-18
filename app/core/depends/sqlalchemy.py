from orm.core import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession


async def get_session() -> AsyncSession:
    async with async_sessionmaker.begin() as session:
        yield session

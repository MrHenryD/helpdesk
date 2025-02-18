from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.schema import MetaData

from core.settings import settings


async_engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URI.replace("postgresql", "postgresql+asyncpg"),
    future=True,
    connect_args={
        "server_settings": {
            "application_name": settings.NAME,
            "statement_timeout": "30000",
        }
    },
    **(
        {"poolclass": NullPool}
        if settings.IS_TEST_ENVIRONMENT
        else {"pool_size": 5, "max_overflow": 20, "pool_recycle": 1800}
    ),
)
metadata = MetaData()
async_session = sessionmaker(
    bind=async_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

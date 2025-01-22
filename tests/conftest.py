import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.models import Base 

TEST_DATABASE_URL = "postgresql+asyncpg://postgres:123surya456@localhost:5432/fastapi_db"

engine = create_async_engine(TEST_DATABASE_URL, future=True, echo=True)
TestingSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

@pytest.fixture(scope="session", autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture()
async def db_session():
    async with SessionLocal() as session:
        yield session
        await session.close()
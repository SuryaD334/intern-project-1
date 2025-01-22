import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:123surya456@localhost:5432/fastapi_db"
settings = Settings()
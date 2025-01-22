from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from core.services import MessageService
from core.repositories import MessageRepository
from core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# Database connection
engine = create_async_engine(settings.DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

class MessageCreate(BaseModel):
    content: str

class MessageUpdate(BaseModel):
    content: str

@router.post("/messages/")
async def create_message(payload: MessageCreate, db: AsyncSession = Depends(get_db)):
    repo = MessageRepository(db)
    service = MessageService(repo)
    return await service.create_message(payload.content)

@router.get("/messages/")
async def get_all_messages(db: AsyncSession = Depends(get_db)):
    repo = MessageRepository(db)
    service = MessageService(repo)
    return await service.get_all_messages()

@router.get("/messages/{message_id}")
async def get_message(message_id: int, db: AsyncSession = Depends(get_db)):
    repo = MessageRepository(db)
    service = MessageService(repo)
    result = await service.get_message(message_id)
    if not result:
        raise HTTPException(status_code=404, detail="Message not found")
    return result

@router.put("/messages/{message_id}")
async def update_message(message_id: int, payload: MessageUpdate, db: AsyncSession = Depends(get_db)):
    repo = MessageRepository(db)
    service = MessageService(repo)
    return await service.update_message(message_id, payload.content)

@router.delete("/messages/{message_id}")
async def delete_message(message_id: int, db: AsyncSession = Depends(get_db)):
    repo = MessageRepository(db)
    service = MessageService(repo)
    return await service.delete_message(message_id)
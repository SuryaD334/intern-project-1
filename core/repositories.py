from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.models import Message

class MessageRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_message(self, content: str):
        message = Message(content=content)
        self.db.add(message)
        await self.db.commit()
        await self.db.refresh(message)
        return message
    
    async def get_all_messages(self):
        result = await self.db.execute(select(Message))
        return result.scalars().all()

    async def get_message(self, message_id: int):
        result = await self.db.execute(select(Message).filter_by(id=message_id))
        return result.scalar_one_or_none()

    async def update_message(self, message_id: int, content: str):
        message = await self.get_message(message_id)
        if message:
            message.content = content
            await self.db.commit()
            await self.db.refresh(message)
        return message

    async def delete_message(self, message_id: int):
        message = await self.get_message(message_id)
        if message:
            await self.db.delete(message)
            await self.db.commit()
        return message
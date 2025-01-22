from core.repositories import MessageRepository

class MessageService:
    def __init__(self, repo: MessageRepository):
        self.repo = repo

    async def create_message(self, content: str):
        return await self.repo.create_message(content)
    
    async def get_all_messages(self):
        return await self.repo.get_all_messages()

    async def get_message(self, message_id: int):
        return await self.repo.get_message(message_id)

    async def update_message(self, message_id: int, content: str):
        return await self.repo.update_message(message_id, content)

    async def delete_message(self, message_id: int):
        return await self.repo.delete_message(message_id)
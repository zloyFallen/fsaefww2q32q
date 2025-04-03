from aiogram import BaseMiddleware
from aiogram.types import Message
from utils.auth import UserManager

class AccessMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        if not UserManager().is_allowed(event.from_user.id):
            await event.answer("🚫 Доступ запрещен")
            return
        return await handler(event, data)
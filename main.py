import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# Импорты обработчиков
from handlers import common, music, video, admin
from middlewares.auth import AccessMiddleware

async def main():
    # Инициализация бота (токен лучше хранить в .env)
    bot = Bot(token="7640700284:AAHUKq9fZGfbS5B5-b0tKxh8QbQTlebuHic")
    
    # Настройка диспетчера
    dp = Dispatcher(storage=MemoryStorage())
    
    # Подключение middleware
    dp.message.middleware(AccessMiddleware())
    
    # Регистрация роутеров
    routers = [
        common.router,
        music.router,
        video.router,
        admin.router
    ]
    
    for router in routers:
        dp.include_router(router)
    
    # Запуск бота с очисткой очереди
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
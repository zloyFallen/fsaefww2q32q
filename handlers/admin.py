from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from config import ADMIN_IDS
import logging

# Настройка логирования
logger = logging.getLogger(__name__)

router = Router()

def check_admin_access(user_id: int) -> bool:
    """Проверка прав администратора"""
    is_admin = user_id in ADMIN_IDS
    if not is_admin:
        logger.warning(f"Доступ запрещен для пользователя {user_id}")
    return is_admin

@router.message(Command("admin"))
async def admin_panel(message: Message):
    """Главное меню админ-панели"""
    if not check_admin_access(message.from_user.id):
        await message.answer("⛔ Доступ запрещен")
        return

    await message.answer(
        "🔐 <b>Административная панель</b>\n\n"
        "📊 /stats - Статистика бота\n"
        "👥 /users - Управление пользователями\n"
        "📢 /broadcast - Рассылка сообщений",
        parse_mode="HTML"
    )

@router.message(Command("stats"))
async def show_stats(message: Message):
    """Показать статистику"""
    if not check_admin_access(message.from_user.id):
        return

    # Заглушка для статистики (реализуйте свою логику)
    stats = {
        "users": 150,
        "active": 42,
        "requests": 1024
    }
    
    await message.answer(
        f"📈 <b>Статистика бота:</b>\n\n"
        f"👤 Всего пользователей: {stats['users']}\n"
        f"🟢 Активных за сутки: {stats['active']}\n"
        f"🔄 Запросов: {stats['requests']}",
        parse_mode="HTML"
    )

@router.message(Command("users"))
async def manage_users(message: Message):
    """Управление пользователями"""
    if not check_admin_access(message.from_user.id):
        return

    await message.answer(
        "👥 <b>Управление пользователями</b>\n\n"
        "Добавить: /add_user [ID]\n"
        "Удалить: /remove_user [ID]",
        parse_mode="HTML"
    )

# Дополнительные команды можно добавлять ниже
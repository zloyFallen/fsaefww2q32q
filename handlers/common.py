from aiogram import Router, F
from aiogram.types import Message
from keyboards.menus import main_menu  # Импорт из текущей структуры
from utils.auth import UserManager  # Импорт из текущей структуры

router = Router()
user_manager = UserManager()

@router.message(F.text == "⬅️ На главную")
async def back_to_menu(message: Message):
    is_admin = user_manager.is_admin(message.from_user.id)
    await message.answer("Главное меню:", reply_markup=main_menu(is_admin))

@router.message(F.text == "ℹ️ Помощь")
async def show_help(message: Message):
    is_admin = user_manager.is_admin(message.from_user.id)
    help_text = (
        "📌 Как использовать бота:\n\n"
        "• Для загрузки музыки - нажмите 🎵 Скачать музыку\n"
        "• Для поиска треков - нажмите 🔍 Найти трек\n"
        "• Для обработки видео - нажмите 🎥 Видео-эффекты\n"
        "• Для аудио-эффектов - нажмите ✂️ Аудио-эффекты"
    )
    await message.answer(help_text, reply_markup=main_menu(is_admin))
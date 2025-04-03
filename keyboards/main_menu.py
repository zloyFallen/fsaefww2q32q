from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def main_menu(is_admin: bool = False):
    buttons = [
        [KeyboardButton(text="🎵 Скачать музыку")],
        [KeyboardButton(text="🔍 Найти трек")],
        [KeyboardButton(text="🎥 Видео-эффекты")],
        [KeyboardButton(text="✂️ Аудио-эффекты")],
        [KeyboardButton(text="👑 Админ-панель")] if is_admin else None
    ]
    return ReplyKeyboardMarkup(
        keyboard=[b for b in buttons if b is not None],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )

def music_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Яндекс.Музыка", callback_data="yandex_music")],
            [InlineKeyboardButton(text="По названию", callback_data="by_name")]
        ]
    )

def admin_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Статистика", callback_data="stats")],
            [InlineKeyboardButton(text="👥 Управление доступом", callback_data="access_control")]
        ]
    )
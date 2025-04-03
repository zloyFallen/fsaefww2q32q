from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards.menus import music_menu

router = Router()

@router.message(F.text == "🎵 Скачать музыку")
async def download_music(message: Message):
    await message.answer(
        "Выберите источник:",
        reply_markup=music_menu()
    )

@router.callback_query(F.data == "yandex_music")
async def yandex_music(callback: CallbackQuery):
    await callback.message.edit_text(
        "Отправьте ссылку на трек из Яндекс.Музыки:",
        reply_markup=None
    )
    await callback.answer()
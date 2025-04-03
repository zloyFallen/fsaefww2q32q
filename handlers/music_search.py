from aiogram import F
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message

from bot.services.audio_processing import search_music_on_platforms
from bot.utils.storage import save_temp_audio
from config import AUDIO_TEMP_DIR

router = Router()

@router.message(Command("search"))
@router.message(F.text & ~F.text.startswith(('http://', 'https://')))
async def handle_music_search(message: Message):
    try:
        query = message.text if not message.text.startswith('/search') else message.text.replace('/search', '').strip()
        if not query:
            return await message.answer("🔍 Введите название трека для поиска")
        
        await message.answer(f"🔍 Ищу трек: {query}")
        
        # Ищем трек на разных площадках
        audio_data, track_info = await search_music_on_platforms(query)
        if not audio_data:
            return await message.answer("❌ Трек не найден")
        
        # Сохраняем временный файл
        file_path = await save_temp_audio(AUDIO_TEMP_DIR, audio_data, f"{track_info['artist']} - {track_info['title']}")
        
        # Отправляем пользователю
        with open(file_path, 'rb') as audio_file:
            await message.answer_audio(
                audio_file,
                title=track_info['title'],
                performer=track_info['artist'],
                caption=f"🎵 {track_info['artist']} - {track_info['title']}"
            )
            
    except Exception as e:
        logging.error(f"Error in handle_music_search: {e}")
        await message.answer("❌ Произошла ошибка при поиске трека")
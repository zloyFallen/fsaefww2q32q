from aiogram import F
from aiogram import Router, types
from aiogram.filters import Text
from aiogram.types import Message
from urllib.parse import urlparse

from bot.services.yandex_api import download_yandex_music_track
from bot.utils.storage import save_temp_audio
from config import AUDIO_TEMP_DIR

router = Router()

@router.message(Text(startswith=['https://music.yandex.ru', 'music.yandex.ru']))
async def handle_yandex_music_link(message: Message):
    try:
        url = message.text
        # Извлекаем ID трека из URL
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.split('/')
        track_id = path_parts[-1] if path_parts[-1] else path_parts[-2]
        
        await message.answer("⏳ Скачиваю трек...")
        
        # Скачиваем трек
        audio_data, track_info = await download_yandex_music_track(track_id)
        if not audio_data:
            return await message.answer("❌ Не удалось скачать трек")
        
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
        logging.error(f"Error in handle_yandex_music_link: {e}")
        await message.answer("❌ Произошла ошибка при обработке вашего запроса")
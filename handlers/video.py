from aiogram import Router, F
from aiogram.types import Message, VideoNote
from aiogram.enums import ContentType
import logging

from services.video_processing import convert_to_circle
from utils.storage import save_temp_video
from config import VIDEO_TEMP_DIR

router = Router()

@router.message(F.content_type == ContentType.VIDEO)
async def handle_video(message: Message):
    try:
        await message.answer("⏳ Преобразую видео в кружочек...")
        
        # Скачиваем видео
        video_file = await message.bot.get_file(message.video.file_id)
        video_path = await save_temp_video(
            VIDEO_TEMP_DIR,
            video_file.file_id,
            await message.bot.download_file(video_file.file_path)
        )
        
        # Обрабатываем видео
        output_path = await convert_to_circle(video_path)
        
        # Отправляем результат
        with open(output_path, 'rb') as video_file:
            await message.answer_video_note(
                VideoNote(
                    video_note=video_file,
                    length=360,
                    duration=message.video.duration,
                    thumb=message.video.thumbnail
                )
            )
            
    except Exception as e:
        logging.error(f"Error in handle_video: {e}")
        await message.answer("❌ Произошла ошибка при обработке видео")
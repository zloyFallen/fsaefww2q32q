import os
from pathlib import Path
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Получаем значения из переменных окружения (правильный способ)
BOT_TOKEN = os.getenv('BOT_TOKEN')  # Ключ должен совпадать с именем в .env
ADMIN_IDS = list(map(int, os.getenv('ADMIN_IDS', '').split(',')))  # Для нескольких ID через запятую
YANDEX_MUSIC_TOKEN = os.getenv('YANDEX_MUSIC_TOKEN')

# Пути к папкам (более надежный вариант с pathlib)
BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / 'logs'
TEMP_DIR = BASE_DIR / 'temp'
AUDIO_TEMP_DIR = TEMP_DIR / 'audio'
VIDEO_TEMP_DIR = TEMP_DIR / 'video'

# Создаем папки (с проверкой прав)
for folder in [LOG_DIR, AUDIO_TEMP_DIR, VIDEO_TEMP_DIR]:
    folder.mkdir(parents=True, exist_ok=True)
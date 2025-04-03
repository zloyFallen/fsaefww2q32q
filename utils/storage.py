import os
from datetime import datetime
import hashlib

async def save_temp_audio(directory: str, audio_data: bytes, filename: str):
    """Сохраняет временный аудиофайл"""
    os.makedirs(directory, exist_ok=True)
    
    # Создаем уникальное имя файла
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    hash_str = hashlib.md5(audio_data).hexdigest()[:8]
    safe_filename = ''.join(c if c.isalnum() else '_' for c in filename)
    file_path = os.path.join(directory, f"{safe_filename}_{timestamp}_{hash_str}.mp3")
    
    with open(file_path, 'wb') as f:
        f.write(audio_data)
        
    return file_path

async def save_temp_video(directory: str, file_id: str, video_data: bytes):
    """Сохраняет временный видеофайл"""
    os.makedirs(directory, exist_ok=True)
    
    # Создаем уникальное имя файла
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    hash_str = hashlib.md5(video_data).hexdigest()[:8]
    file_path = os.path.join(directory, f"{file_id}_{timestamp}_{hash_str}.mp4")
    
    with open(file_path, 'wb') as f:
        f.write(video_data)
        
    return file_path
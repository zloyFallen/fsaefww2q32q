import logging
from moviepy.editor import VideoFileClip
import numpy as np
import cv2
import os

async def convert_to_circle(video_path: str):
    """Преобразует видео в круглый формат (VideoNote)"""
    try:
        output_path = video_path.replace('.mp4', '_circle.mp4')
        
        # Загружаем видео
        clip = VideoFileClip(video_path)
        
        # Создаем маску круга
        def make_circle_frame(frame):
            height, width = frame.shape[:2]
            mask = np.zeros((height, width), dtype=np.uint8)
            cv2.circle(mask, (width//2, height//2), min(width, height)//2, 255, -1)
            
            # Применяем маску
            result = cv2.bitwise_and(frame, frame, mask=mask)
            return result
            
        # Применяем эффект к каждому кадру
        circle_clip = clip.fl_image(make_circle_frame)
        
        # Сохраняем результат
        circle_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        
        return output_path
        
    except Exception as e:
        logging.error(f"Error in convert_to_circle: {e}")
        return None
    finally:
        if 'clip' in locals():
            clip.close()
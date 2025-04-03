import logging
import yt_dlp
import requests

async def search_music_on_platforms(query: str):
    """Ищет музыку на разных площадках (YouTube, SoundCloud и др.)"""
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'extract_flat': True,
            'default_search': 'ytsearch',
            'noplaylist': True
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            if not info or 'entries' not in info or not info['entries']:
                return None, None
                
            # Берем первый результат
            track_info = info['entries'][0]
            audio_url = track_info['url']
            
            # Скачиваем аудио
            response = requests.get(audio_url)
            if response.status_code != 200:
                return None, None
                
            metadata = {
                'title': track_info.get('title', 'Unknown'),
                'artist': track_info.get('uploader', 'Unknown'),
                'duration': track_info.get('duration', 0)
            }
            
            return response.content, metadata
            
    except Exception as e:
        logging.error(f"Error in search_music_on_platforms: {e}")
        return None, None
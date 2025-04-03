import logging
from yandex_music import Client

from config import YANDEX_MUSIC_TOKEN

async def download_yandex_music_track(track_id: str):
    """Скачивает трек с Яндекс.Музыки по ID"""
    try:
        client = Client(YANDEX_MUSIC_TOKEN).init()
        
        # Получаем информацию о треке
        track = client.tracks(track_id)[0]
        track_info = {
            'title': track.title,
            'artist': ', '.join([artist.name for artist in track.artists]),
            'album': track.albums[0].title if track.albums else 'Unknown'
        }
        
        # Получаем URL для скачивания
        download_info = track.get_download_info(get_direct_links=True)
        if not download_info:
            return None, None
            
        # Выбираем максимальное качество
        best_quality = max(download_info, key=lambda x: x.bitrate_in_kbps)
        direct_link = best_quality.direct_link
        
        # Скачиваем трек
        import requests
        response = requests.get(direct_link)
        if response.status_code != 200:
            return None, None
            
        return response.content, track_info
        
    except Exception as e:
        logging.error(f"Error in download_yandex_music_track: {e}")
        return None, None
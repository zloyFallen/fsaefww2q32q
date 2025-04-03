import logging
from datetime import datetime
from pathlib import Path

def setup_logger(log_dir: str):
    """Настройка логгера для записи в файл и консоль"""
    log_file = Path(log_dir) / 'bot.log'
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    # Логирование начала работы
    logging.info('Bot started')
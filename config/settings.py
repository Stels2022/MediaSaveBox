from pathlib import Path

from dotenv import load_dotenv

import os

# Корневая папка проекта
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# Папки
DOWNLOAD_DIR = BASE_DIR / "downloads"
TEMP_DIR = BASE_DIR / "temp"
LOG_DIR = BASE_DIR / "logs"
KEYBOARDS_DIR = BASE_DIR / "keyboards"

BOT_TOKEN = os.getenv("BOT_TOKEN")
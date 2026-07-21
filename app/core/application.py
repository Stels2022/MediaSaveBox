from app.services.directory_service import DirectoryService
import logging

from app.services.directory_service import DirectoryService
from app.services.logger_service import LoggerService
from app.bot.bot import TelegramBot

class Application:
    """
    Главный класс приложения.
    Отвечает за запуск MediaSaveBox.
    """

    VERSION = "0.1.0"

    def __init__(self):
        print("=" * 45)
        print(f"      MediaSaveBox v{self.VERSION}")
        print("=" * 45)

        self.bot = TelegramBot()

    def run(self):
        DirectoryService.ensure_directories()

        LoggerService.initialize()

        logging.info("Application started.")

        self.bot.run()
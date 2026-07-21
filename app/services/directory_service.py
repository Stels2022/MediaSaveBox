from config.settings import DOWNLOAD_DIR, TEMP_DIR, LOG_DIR


class DirectoryService:
    """
    Отвечает за подготовку структуры директорий приложения.
    """

    @staticmethod
    def ensure_directories():
        """
        Проверяет наличие необходимых директорий.
        Если директория отсутствует — создаёт её.
        """

        directories = (
            DOWNLOAD_DIR,
            TEMP_DIR,
            LOG_DIR,
        )

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
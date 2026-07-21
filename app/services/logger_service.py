import logging

from config.settings import LOG_DIR


class LoggerService:
    """
    Отвечает за настройку логирования приложения.
    """

    @staticmethod
    def initialize():

        log_file = LOG_DIR / "mediasavebox.log"

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.FileHandler(log_file, encoding="utf-8"),
                logging.StreamHandler()
            ]
        )

        logging.info("Logger initialized.")
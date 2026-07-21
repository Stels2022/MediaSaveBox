from abc import ABC, abstractmethod


class BaseDownloader(ABC):
    """
    Базовый класс для всех Downloader.
    """

    @abstractmethod
    async def download(self, url: str):
        """
        Скачать файл по URL.
        """
        pass
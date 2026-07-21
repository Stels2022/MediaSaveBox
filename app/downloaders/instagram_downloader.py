import logging

from app.downloaders.base_downloader import BaseDownloader


class InstagramDownloader(BaseDownloader):

    async def download(self, url: str):

        logging.info(f"Downloading Instagram: {url}")

        return None
import logging

from app.downloaders.base_downloader import BaseDownloader


class PinterestDownloader(BaseDownloader):

    async def download(self, url: str):

        logging.info(f"Downloading Pinterest: {url}")

        return None
import logging

from app.downloaders.base_downloader import BaseDownloader


class TikTokDownloader(BaseDownloader):

    async def download(self, url: str):

        logging.info(f"Downloading TikTok: {url}")

        return None
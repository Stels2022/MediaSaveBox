import logging

from app.downloaders.base_downloader import BaseDownloader


class YoutubeDownloader(BaseDownloader):

    async def download(self, url: str):

        logging.info(f"Downloading YouTube: {url}")

        return None
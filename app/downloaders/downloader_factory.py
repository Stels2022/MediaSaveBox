from app.models.platform import Platform

from app.downloaders.instagram_downloader import InstagramDownloader
from app.downloaders.youtube_downloader import YoutubeDownloader
from app.downloaders.tiktok_downloader import TikTokDownloader
from app.downloaders.pinterest_downloader import PinterestDownloader


class DownloaderFactory:

    @staticmethod
    def create(platform: Platform):

        if platform == Platform.INSTAGRAM:
            return InstagramDownloader()

        if platform == Platform.YOUTUBE:
            return YoutubeDownloader()

        if platform == Platform.TIKTOK:
            return TikTokDownloader()

        if platform == Platform.PINTEREST:
            return PinterestDownloader()

        return None
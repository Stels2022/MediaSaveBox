import logging
from pprint import pprint

import yt_dlp

from app.models.media_info import MediaInfo
from app.models.platform import Platform



class MediaInfoService:
    """
    Получение информации о медиа без скачивания.
    """

    def __init__(self):
        self.ydl_opts = {
            "quiet": True,
            "no_warnings": True,
        }

    @staticmethod
    def format_duration(seconds: int) -> str:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        if hours > 0:
            return f"{hours}:{minutes:02}:{secs:02}"

        return f"{minutes}:{secs:02}"

    async def get_info(
        self,
        url: str,
        platform: Platform
    ) -> MediaInfo | None:

        logging.info(f"Getting media info: {url}")

        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(
                url,
                download=False
            )

        pprint(info)

        return MediaInfo(
            title=info.get("title", ""),
            author=info.get("uploader", ""),
            duration=info.get("duration", 0),
            duration_string=self.format_duration(
                info.get("duration", 0)
            ),
            views=info.get("view_count", 0),
            url=info.get("webpage_url", url),
            thumbnail=info.get("thumbnail", ""),
            platform=platform
        )

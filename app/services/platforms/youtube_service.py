import logging
import asyncio
from pprint import pprint

import yt_dlp

from app.models.media_info import MediaInfo
from app.models.platform import Platform
from app.models.media_type import MediaType
from yt_dlp.utils import DownloadError



class YouTubeService:
    """
    Получение информации о медиа без скачивания.
    """

    def __init__(self):
        self.ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "socket_timeout": 10,
        }

    @staticmethod
    def format_duration(seconds: int) -> str:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        if hours > 0:
            return f"{hours}:{minutes:02}:{secs:02}"

        return f"{minutes}:{secs:02}"

    def _extract_info(self, url: str):

        logging.info("Create YoutubeDL")

        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:

                logging.info("Calling extract_info")

                result = ydl.extract_info(
                    url,
                    download=False
                )

                logging.info("extract_info finished")

                return result

        except DownloadError as e:
            logging.exception(e)
            return None

        except Exception:
            logging.exception("Unexpected error")
            return None

    def _detect_media_type(self, info: dict) -> MediaType:
        """
        Определяет тип медиа по данным yt-dlp.
        """

        # Галерея / плейлист
        if info.get("entries"):
            return MediaType.GALLERY

        ext = (info.get("ext") or "").lower()
        vcodec = info.get("vcodec")
        acodec = info.get("acodec")

        # Изображения
        if ext in ("jpg", "jpeg", "png", "gif", "webp"):
            return MediaType.IMAGE

        # Видео
        if vcodec and vcodec != "none":
            return MediaType.VIDEO

        # Только аудио
        if acodec and acodec != "none":
            return MediaType.AUDIO

        return MediaType.UNKNOWN

    async def get_info(
            self,
            url: str,
            platform: Platform
    ) -> MediaInfo | None:

        logging.info(f"Getting media info: {url}")

        info = await asyncio.to_thread(
            self._extract_info,
            url
        )

        if info is None:
            logging.warning("Media info not found.")
            return None

        pprint(info)

        return MediaInfo(
            title=info.get("title", ""),
            author=info.get("uploader", ""),
            media_type=self._detect_media_type(info),
            duration=info.get("duration", 0),
            duration_string=self.format_duration(
                info.get("duration", 0)
            ),
            views=info.get("view_count", 0),
            url=info.get("webpage_url", url),
            thumbnail=info.get("thumbnail", ""),
            platform=platform
        )

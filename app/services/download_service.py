import logging
import asyncio
from pathlib import Path

import yt_dlp


class DownloadService:

    def __init__(self):
        self.temp_dir = Path("temp")
        self.temp_dir.mkdir(exist_ok=True)

    async def download_video(self, url: str) -> Path:
        return await asyncio.to_thread(
            self._download_video,
            url
        )

    def _download_video(self, url: str) -> Path:
        logging.info("Downloading video...")

        output = self.temp_dir / "%(id)s.%(ext)s"

        ydl_opts = {
            "format": "bv*+ba/b",
            "merge_output_format": "mp4",
            "outtmpl": str(output),
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                url,
                download=True
            )

            filename = Path(
                ydl.prepare_filename(info)
            )

            if filename.suffix != ".mp4":
                filename = filename.with_suffix(".mp4")

            return filename

    async def download_audio(self, url: str) -> Path:
        return await asyncio.to_thread(
            self._download_audio,
            url
        )

    def _download_audio(self, url: str) -> Path:

        logging.info("Downloading audio...")

        output = self.temp_dir / "%(id)s.%(ext)s"

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": str(output),
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,

            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=True
            )

            return Path(
                ydl.prepare_filename(info)
            ).with_suffix(".mp3")
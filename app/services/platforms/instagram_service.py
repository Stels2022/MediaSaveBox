import asyncio
import logging
import subprocess
from pathlib import Path

from app.models.media_info import MediaInfo
from app.models.media_type import MediaType
from app.models.platform import Platform


class InstagramService:

    def __init__(self):

        self.download_dir = Path(
            "downloads/instagram"
        )

        self.download_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.cookies = Path(
            "cookies/instagram.txt"
        )


    async def get_info(
        self,
        url: str,
        platform: Platform
    ) -> MediaInfo | None:

        logging.info(
            f"Downloading Instagram media: {url}"
        )

        files = await asyncio.to_thread(
            self._download,
            url
        )

        logging.info(
            f"Downloaded files: {files}"
        )

        if not files:
            return None


        return MediaInfo(
            title="Instagram",
            author="Instagram",
            media_type=self._detect_media_type(files),
            duration=0,
            duration_string="",
            views=0,
            url=url,
            thumbnail="",
            platform=platform,
            files=files
        )


    def _download(
        self,
        url: str
    ) -> list[Path]:

        cmd = [
            "gallery-dl",
            "--cookies",
            str(self.cookies),
            "-D",
            str(self.download_dir),
            url
        ]


        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )


        logging.info(
            result.stdout
        )

        if result.stderr:
            logging.error(
                result.stderr
            )


        if result.returncode != 0:
            return []


        return self._parse_files(
            result.stdout
        )


    @staticmethod
    def _parse_files(
        stdout: str
    ) -> list[Path]:

        files = []


        for line in stdout.splitlines():

            line = line.strip()

            if not line:
                continue


            path = Path(line)


            if path.suffix.lower() in (
                ".jpg",
                ".jpeg",
                ".png",
                ".webp",
                ".gif",
                ".mp4",
                ".mov",
                ".mkv",
                ".webm"
            ):
                files.append(path)


        return files


    @staticmethod
    def _detect_media_type(
        files: list[Path]
    ) -> MediaType:

        if len(files) > 1:
            return MediaType.GALLERY


        ext = files[0].suffix.lower()


        if ext in (
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
            ".gif"
        ):
            return MediaType.IMAGE


        if ext in (
            ".mp4",
            ".mov",
            ".mkv",
            ".webm"
        ):
            return MediaType.VIDEO


        return MediaType.UNKNOWN
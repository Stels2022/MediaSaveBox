import asyncio
import logging
from pathlib import Path

from gallery_dl import config, job


class GalleryDLService:
    """
    Сервис для скачивания медиа через gallery-dl.

    Используется:
        - Instagram
        - Pinterest
        - (в будущем Threads и др.)
    """

    def __init__(
        self,
        download_dir: str = "downloads",
        cookies: str | None = None
    ):

        self.download_dir = Path(download_dir)

        self.download_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        config.set(("base-directory",), str(self.download_dir))

        if cookies:
            config.set(
                ("extractor", "cookies"),
                cookies
            )

    async def download(
        self,
        url: str
    ) -> list[Path]:

        return await asyncio.to_thread(
            self._download,
            url
        )

    def _download(
        self,
        url: str
    ) -> list[Path]:

        logging.info(f"gallery-dl download: {url}")

        before = {
            file
            for file in self.download_dir.rglob("*")
            if file.is_file()
        }

        download_job = job.DownloadJob(url)

        download_job.run()

        after = {
            file
            for file in self.download_dir.rglob("*")
            if file.is_file()
        }

        files = sorted(after - before)

        logging.info(
            f"gallery-dl downloaded {len(files)} file(s)"
        )

        return files
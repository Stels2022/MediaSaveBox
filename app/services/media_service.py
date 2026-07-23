from app.models.platform import Platform
from app.models.media_info import MediaInfo

from app.services.platforms.youtube_service import YouTubeService
from app.services.platforms.instagram_service import InstagramService
from app.services.platforms.tiktok_service import TikTokService
from app.services.platforms.pinterest_service import PinterestService


SERVICES = {
    Platform.YOUTUBE: YouTubeService,
    Platform.INSTAGRAM: InstagramService,
    Platform.TIKTOK: TikTokService,
    Platform.PINTEREST: PinterestService,
}


class MediaService:

    async def get_info(
        self,
        url: str,
        platform: Platform
    ) -> MediaInfo | None:

        service_class = SERVICES.get(platform)

        if service_class is None:
            return None

        service = service_class()

        return await service.get_info(
            url,
            platform
        )
from dataclasses import dataclass

from app.models.platform import Platform
from app.models.media_type import MediaType


@dataclass
class MediaInfo:

    title: str
    author: str

    media_type: MediaType

    duration: int
    duration_string: str

    views: int

    url: str

    thumbnail: str

    platform: Platform
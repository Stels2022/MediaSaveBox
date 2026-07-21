from dataclasses import dataclass

from app.models.platform import Platform


@dataclass
class MediaInfo:
    """
    Информация о медиафайле.
    """

    title: str
    author: str
    duration: int
    url: str
    thumbnail: str
    platform: Platform
    views: int
    duration_string: str
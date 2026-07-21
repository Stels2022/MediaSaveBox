from enum import Enum


class Platform(Enum):
    """
    Поддерживаемые платформы.
    """

    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    YOUTUBE = "youtube"
    PINTEREST = "pinterest"

    UNKNOWN = "unknown"
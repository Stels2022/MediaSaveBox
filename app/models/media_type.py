from enum import Enum


class MediaType(Enum):
    VIDEO = "video"
    AUDIO = "audio"
    IMAGE = "image"
    GALLERY = "gallery"
    UNKNOWN = "unknown"
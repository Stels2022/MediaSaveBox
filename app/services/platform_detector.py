from app.models.platform import Platform


class PlatformDetector:
    """
    Определяет платформу по тексту сообщения.
    """

    DOMAINS = {
        Platform.INSTAGRAM: [
            "instagram.com",
        ],
        Platform.TIKTOK: [
            "tiktok.com",
            "vm.tiktok.com",
            "vt.tiktok.com",
        ],
        Platform.YOUTUBE: [
            "youtube.com",
            "youtu.be",
            "m.youtube.com",
        ],
        Platform.PINTEREST: [
            "pinterest.com",
            "pin.it",
        ],
    }

    @classmethod
    def detect(cls, text: str) -> Platform:

        text = text.lower()

        for platform, domains in cls.DOMAINS.items():
            for domain in domains:
                if domain in text:
                    return platform

        return Platform.UNKNOWN
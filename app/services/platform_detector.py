from app.models.platform import Platform


class PlatformDetector:
    """
    Определяет платформу по тексту сообщения.
    """

    @staticmethod
    def detect(text: str) -> Platform:
        """
        Возвращает тип платформы.
        """

        text = text.lower()

        if "instagram.com" in text:
            return Platform.INSTAGRAM

        if "tiktok.com" in text:
            return Platform.TIKTOK

        if "youtu.be" in text or "youtube.com" in text:
            return Platform.YOUTUBE

        if "pinterest." in text:
            return Platform.PINTEREST

        return Platform.UNKNOWN
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

from app.models.media_info import MediaInfo
from app.models.media_type import MediaType


class DownloadKeyboard:

    @staticmethod
    def create(media: MediaInfo):

        keyboard = []

        if media.media_type == MediaType.VIDEO:

            keyboard = [
                [
                    InlineKeyboardButton(
                        "🎥 MP4",
                        callback_data="download_video"
                    ),
                    InlineKeyboardButton(
                        "🎵 MP3",
                        callback_data="download_audio"
                    )
                ]
            ]

        elif media.media_type == MediaType.IMAGE:

            keyboard = [
                [
                    InlineKeyboardButton(
                        "🖼 Скачать",
                        callback_data="download_image"
                    )
                ]
            ]

        elif media.media_type == MediaType.AUDIO:

            keyboard = [
                [
                    InlineKeyboardButton(
                        "🎵 Скачать",
                        callback_data="download_audio"
                    )
                ]
            ]

        elif media.media_type == MediaType.GALLERY:

            keyboard = [
                [
                    InlineKeyboardButton(
                        "📷 Скачать галерею",
                        callback_data="download_gallery"
                    )
                ]
            ]

        return InlineKeyboardMarkup(keyboard)
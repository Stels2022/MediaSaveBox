from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


class DownloadKeyboard:

    @staticmethod
    def create():

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

        return InlineKeyboardMarkup(keyboard)
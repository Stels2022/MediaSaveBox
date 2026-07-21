import logging

from telegram import Update
from telegram.ext import ContextTypes

from app.services.media_cache import MediaCache
from app.services.download_service import DownloadService

download_service = DownloadService()


async def callback_handler(update: Update,
                           context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    logging.info(query.data)

    media = MediaCache.get(
        query.message.message_id
    )

    if media is None:

        await query.edit_message_text(
            "❌ Информация о видео не найдена."
        )

        return

    if query.data == "download_video":

        file = await download_service.download_video(
            media.url
        )

        try:

            with open(file, "rb") as video:

                await query.message.reply_video(
                    video=video,
                    caption=media.title
                )

        finally:

            if file.exists():
                file.unlink()


    elif query.data == "download_audio":

        file = await download_service.download_audio(
            media.url
        )

        try:

            with open(file, "rb") as audio:

                await query.message.reply_audio(
                    audio=audio,
                    title=media.title,
                    performer=media.author
                )

        finally:

            if file.exists():
                file.unlink()
import logging

from telegram import Update
from telegram.ext import ContextTypes

from app.services.media_cache import MediaCache
from app.services.download_service import DownloadService
from app.services.chat_action_service import ChatActionService

download_service = DownloadService()
chat_action = ChatActionService()


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
        await chat_action.typing(query.message.chat)
        file = await download_service.download_video(
            media.url
        )

        try:
            await chat_action.upload_video(query.message.chat)
            with open(file, "rb") as video:

                await query.message.reply_video(
                    video=video,
                    caption=media.title
                )

        finally:

            if file.exists():
                file.unlink()


    elif query.data == "download_audio":
        await chat_action.typing(
            query.message.chat
        )
        file = await download_service.download_audio(
            media.url
        )

        try:
            await chat_action.upload_audio(
                query.message.chat
            )
            with open(file, "rb") as audio:

                await query.message.reply_audio(
                    audio=audio,
                    title=media.title,
                    performer=media.author
                )

        finally:

            if file.exists():
                file.unlink()

    elif query.data == "download_image":

        await query.message.reply_text(
            "🖼 Скачивание изображения пока в разработке."
        )

    elif query.data == "download_gallery":

        await query.message.reply_text(
            "📷 Скачивание галереи пока в разработке."
        )
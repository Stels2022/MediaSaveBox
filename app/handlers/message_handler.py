import asyncio
import logging

from telegram import Update
from telegram.ext import ContextTypes

from app.models.download_status import DownloadStatus
from app.services.message_service import MessageService
from app.services.platform_detector import PlatformDetector
from app.services.media_info_service import MediaInfoService
from app.keyboards.download_keyboard import DownloadKeyboard
from app.services.media_cache import MediaCache

message_service = MessageService()
media_info_service = MediaInfoService()


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    logging.info(f"Received message: {text}")

    status_message = await message_service.send_status(
        update,
        DownloadStatus.RECEIVED
    )

    await asyncio.sleep(0.5)

    await message_service.edit_status(
        status_message,
        DownloadStatus.DETECTING
    )

    platform = PlatformDetector.detect(text)
    if platform != platform.UNKNOWN:
        media = await media_info_service.get_info(
            text,
            platform
        )

        logging.info(media)

    logging.info(f"Detected platform: {platform.value}")

    await asyncio.sleep(0.5)

    await status_message.edit_text(
        f"✅ Платформа определена: {platform.value}"
    )

    message = await update.message.reply_text(
        f"🎬 {media.title}\n\n"
        f"👤 {media.author}\n"
        f"⏱ {media.duration_string}\n"
        f"👀 {media.views:,}",
        reply_markup=DownloadKeyboard.create()
    )

    MediaCache.save(
        message.message_id,
        media
    )
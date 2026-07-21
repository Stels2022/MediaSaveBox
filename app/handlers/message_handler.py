import asyncio
import logging

from telegram import Update
from telegram.ext import ContextTypes

from app.models.download_status import DownloadStatus
from app.services.message_service import MessageService
from app.services.platform_detector import PlatformDetector

message_service = MessageService()


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

    logging.info(f"Detected platform: {platform.value}")

    await asyncio.sleep(0.5)

    await status_message.edit_text(
        f"✅ Платформа определена: {platform.value}"
    )
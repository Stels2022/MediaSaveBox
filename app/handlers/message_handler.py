import logging

from telegram import Update
from telegram.ext import ContextTypes

from app.models.download_status import DownloadStatus
from app.models.media_type import MediaType
from app.models.platform import Platform
from app.services.message_service import MessageService
from app.services.platform_detector import PlatformDetector
from app.services.media_service import MediaService
from app.keyboards.download_keyboard import DownloadKeyboard
from app.services.chat_action_service import ChatActionService
from app.services.media_cache import MediaCache

message_service = MessageService()
media_service = MediaService()
chat_action = ChatActionService()


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text.strip()

    logging.info(f"Received message: {text}")

    status_message = await message_service.send_status(
        update,
        DownloadStatus.RECEIVED
    )

    await message_service.edit_status(
        status_message,
        DownloadStatus.DETECTING
    )

    platform = PlatformDetector.detect(text)

    if platform == Platform.UNKNOWN:

        await status_message.edit_text(
            "❌ Данная платформа пока не поддерживается."
        )

        return

    await chat_action.typing(
        update.effective_chat
    )

    media = await media_service.get_info(
        text,
        platform
    )

    if media is None:

        await status_message.edit_text(
            "❌ Не удалось получить информацию о медиа."
        )

        return

    logging.info(media)

    #
    # Instagram / Pinterest
    # Сразу отправляем скачанные файлы
    #
    if platform in (
        Platform.INSTAGRAM,
        Platform.PINTEREST
    ):

        await status_message.delete()

        for file in media.files:

            suffix = file.suffix.lower()

            try:

                if media.media_type == MediaType.IMAGE:

                    with open(file, "rb") as f:

                        await update.message.reply_photo(
                            photo=f
                        )

                elif media.media_type == MediaType.VIDEO:

                    with open(file, "rb") as f:

                        await update.message.reply_video(
                            video=f
                        )

                elif media.media_type == MediaType.GALLERY:

                    if suffix in (
                        ".jpg",
                        ".jpeg",
                        ".png",
                        ".webp"
                    ):

                        with open(file, "rb") as f:

                            await update.message.reply_photo(
                                photo=f
                            )

                    else:

                        with open(file, "rb") as f:

                            await update.message.reply_video(
                                video=f
                            )

            except Exception as e:

                logging.exception(e)

        return

    #
    # YouTube / TikTok
    #

    await status_message.edit_text(
        f"✅ Платформа определена: {platform.value}"
    )

    message = await update.message.reply_text(
        f"🎬 {media.title}\n\n"
        f"👤 {media.author}\n"
        f"⏱ {media.duration_string}\n"
        f"👀 {media.views:,}",
        reply_markup=DownloadKeyboard.create(media)
    )

    MediaCache.save(
        message.message_id,
        media
    )
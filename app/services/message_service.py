from telegram import Message, Update

from app.models.download_status import DownloadStatus


class MessageService:

    STATUS_MESSAGES = {
        DownloadStatus.RECEIVED: "📥 Получил ссылку.",
        DownloadStatus.DETECTING: "🔍 Определяю платформу...",
        DownloadStatus.DOWNLOADING: "⬇️ Скачиваю видео...",
        DownloadStatus.SENDING: "📤 Отправляю файл...",
        DownloadStatus.DONE: "✅ Готово!",
        DownloadStatus.ERROR: "❌ Произошла ошибка.",
    }

    async def send_status(
        self,
        update: Update,
        status: DownloadStatus,
    ) -> Message:

        return await update.message.reply_text(
            self.STATUS_MESSAGES[status]
        )

    async def edit_status(
        self,
        message: Message,
        status: DownloadStatus,
    ):

        await message.edit_text(
            self.STATUS_MESSAGES[status]
        )

    async def edit_text(
            self,
            message: Message,
            text: str,
    ):
        await message.edit_text(text)
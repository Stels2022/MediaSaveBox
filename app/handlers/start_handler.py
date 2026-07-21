import logging

from telegram import Update
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработчик команды /start
    """

    logging.info("/start command received")

    await update.message.reply_text(
        "👋 Привет!\n\n"
        "Я MediaSaveBox.\n\n"
        "Отправь мне ссылку на:\n"
        "• Instagram\n"
        "• TikTok\n"
        "• Pinterest\n"
        "• YouTube\n\n"
        "И я сохраню её для тебя 😊"
    )
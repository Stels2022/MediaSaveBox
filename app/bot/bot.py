from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from app.handlers.start_handler import start_command

from telegram.ext import MessageHandler, filters
from app.handlers.message_handler import message_handler

from config.settings import BOT_TOKEN
import logging


class TelegramBot:
    """
    Управляет Telegram-ботом.
    """

    def __init__(self):
        self.application = (
            ApplicationBuilder()
            .token(BOT_TOKEN)
            .build()
        )
        self.application.add_handler(
            CommandHandler("start", start_command)
        )
        self.application.add_handler(
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                message_handler
            )
        )

    def run(self):
        logging.info("Starting Telegram Bot...")

        self.application.run_polling()
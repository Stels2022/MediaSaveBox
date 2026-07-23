from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from app.handlers.start_handler import start_command

from telegram.ext import MessageHandler, filters
from app.handlers.message_handler import message_handler
from telegram.ext import CallbackQueryHandler
from app.handlers.callback_handler import callback_handler

from config.settings import BOT_TOKEN
import logging


class TelegramBot:

    def __init__(self):
        self.application = (
            ApplicationBuilder()
            .token(BOT_TOKEN)
            .read_timeout(120)
            .write_timeout(120)
            .connect_timeout(30)
            .pool_timeout(30)
            .build()
        )

        self.register_handlers()

    def register_handlers(self):

        self.application.add_handler(
            CommandHandler("start", start_command)
        )

        self.application.add_handler(
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                message_handler
            )
        )

        self.application.add_handler(
            CallbackQueryHandler(callback_handler)
        )

    def run(self):
        logging.info("Starting Telegram Bot...")
        self.application.run_polling()
from telegram import Chat
from telegram.constants import ChatAction


class ChatActionService:
    """
    Отправляет пользователю статус действия.
    """

    async def typing(self, chat: Chat):

        await chat.send_action(
            ChatAction.TYPING
        )

    async def upload_video(self, chat: Chat):

        await chat.send_action(
            ChatAction.UPLOAD_VIDEO
        )

    async def upload_audio(self, chat: Chat):
        await chat.send_action(
            ChatAction.UPLOAD_DOCUMENT
        )

    async def upload_document(self, chat: Chat):

        await chat.send_action(
            ChatAction.UPLOAD_DOCUMENT
        )
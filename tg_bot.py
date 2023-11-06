import os

from dotenv import load_dotenv
from tg_api import (
    SyncTgClient,
    SendMessageRequest,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    SendBytesPhotoRequest
)


def send_message(bot_token, tg_chat_id):
    with SyncTgClient.setup(bot_token):
        tg_request = SendMessageRequest(chat_id=tg_chat_id, text='Message proofs high level usage.')
        tg_request.send()


def send_message_keyboard(bot_token, tg_chat_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='button_1', callback_data='test'),
                InlineKeyboardButton(text='button_2', callback_data='test'),
            ],
        ],
    )
    with SyncTgClient.setup(bot_token):
        tg_request = SendMessageRequest(
            chat_id=tg_chat_id,
            text='Message proofs keyboard support.',
            reply_markup=keyboard,
        )
        tg_request.send()


def send_message_photo(bot_token, tg_chat_id, photo_filename):
    with SyncTgClient.setup(bot_token):
        with open(photo_filename, 'rb') as f:
            photo_content = f.read()
        tg_request = SendBytesPhotoRequest(chat_id=tg_chat_id, photo=photo_content, filename=photo_filename)
        tg_request.send()


if __name__ == "__main__":
    load_dotenv()
    bot_token = os.environ["TG_BOT_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    photo_filename = "PHOTO_FILE"

    send_message(bot_token, tg_chat_id)
    send_message_keyboard(bot_token, tg_chat_id)
    send_message_photo(bot_token, tg_chat_id, photo_filename)

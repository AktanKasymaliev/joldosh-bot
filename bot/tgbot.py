import os

import telebot
from telebot import types
from telebot.types import Message
from .api import download_image

from configurations import config, get_messages

config()

MESSAGES = get_messages()
tgbot = telebot.TeleBot(os.environ.get("TOKEN"), parse_mode=None)
USER_DATA = {}
PHOTOS = []

@tgbot.message_handler(commands=['start'])
def start(message: Message):

    markup = types.ReplyKeyboardMarkup(row_width=2, 
                                        resize_keyboard=True, 
                                        one_time_keyboard=True)
    b1 = types.KeyboardButton(MESSAGES["Peshkom"][1])
    b2 = types.KeyboardButton(MESSAGES["Peshkom"][2])
    b3 = types.KeyboardButton(MESSAGES["Peshkom"][3])
    b4 = types.KeyboardButton(MESSAGES["Peshkom"][4])
    b5 = types.KeyboardButton(MESSAGES["Peshkom"][5])
    b6 = types.KeyboardButton("Другое...")
    markup.add(b1, b2, b3, b4, b5, b6)

    tgbot.send_message(
        message.chat.id, 
        MESSAGES.get("HI", None).format(message.chat.first_name),
        reply_markup=markup
        )
    
@tgbot.message_handler(content_types=["text"])
def save_description(message: Message):
    if message.text == "Другое...":
        tgbot.reply_to(message, "Опишите пожалуйста проблему.")
        USER_DATA["problem"] = message.text
    else:
        tgbot.send_message(message.chat.id, "Прикрепите пожалуйста геолокацию.")
        USER_DATA["problem"] = message.text

@tgbot.message_handler(content_types=["location"])
def get_geolocation(message: Message):
    if message.location:
        tgbot.send_message(message.chat.id, "Прикрепите пожалуйста фотографию.")
        USER_DATA["latitude"] = message.location.latitude
        USER_DATA["longitude"] = message.location.longitude


@tgbot.message_handler(content_types=["photo"])
def get_photos(message: Message):

    # markup = types.InlineKeyboardMarkup(row_width=2)
    # b1 = types.InlineKeyboardButton("Да!", callback_data="cb_yes")
    # b2 = types.InlineKeyboardButton("Нет.", callback_data="cb_no")
    # markup.add(b1, b2)

    for _ in message.photo:
        PHOTOS.append(message.photo[-1])
        break

    download_image(tgbot, message, PHOTOS, USER_DATA)
    tgbot.send_message(message.chat.id, "Спасибо вам большое за неравнодушье!!!")

# @tgbot.callback_query_handler(func=lambda call: True)
# def save_photo(call):
#     if call.data == "cb_yes":
#         tgbot.send_message(call.from_user.id, "Прикрепите пожалуйста фотографию.")
#     elif call.data == "cb_no":
#         tgbot.send_message(call.from_user.id, "Спасибо вам большое за неравнодушье!!!")

#     tgbot.delete_message(call.message.chat.id, call.message.message_id)

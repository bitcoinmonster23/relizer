from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
import custom_utils
import os
from decouple import config


app2 = Client(
    'filmy_bot',
    api_id = '1319289' ,
    api_hash = '8f5127ed38135aa349a7384f547a309c' ,
    bot_token = '1263380136:AAG_kErZYKbrBNxpZzxcOlTo32ffLHQOaJQ' ,
)


@app2.on_message(Filters.regex('http'))
def post(client, message):
    if message.chat.username == 'screlizer':
        url = message.text
        text = custom_utils.parsing(url)
        client.send_message(
            'filmy',
            text[0],
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('🎥 Смотреть онлайн!', url=text[1]),
                InlineKeyboardButton('🔎 Поиск фильмов!', url='https://t.me/searchikino_bot')
            ]]),
        )


app2.run()


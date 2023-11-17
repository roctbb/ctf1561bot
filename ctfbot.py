import random

from telebot import TeleBot
from config import token
from flags import *

bot = TeleBot(token)


@bot.message_handler(content_types=['voice'])
def voice_message(message):
    bot.send_message(message.chat.id, FLAG1)


@bot.message_handler(commands=['flag'])
def voice_message(message):
    bot.send_message(message.chat.id, FLAG2)


@bot.message_handler(content_types=['text'])
def check_text(message):
    if message.forward_from:
        bot.send_message(message.chat.id, FLAG3)

    elif message.text.count('1561') > 3:
        bot.send_message(message.chat.id, FLAG4)
    elif message.text.isnumeric():
        x = int(message.text)

        if x * x - 10 * x + 1586 == 1561:
            bot.send_message(message.chat.id, FLAG5)
        else:
            bot.send_message(message.chat.id, "👩‍🏫!")
    elif message.text == FLAG1 + FLAG2 + FLAG3 + FLAG4 + FLAG5 + FLAG6 + FLAG7:
        bot.send_message(message.chat.id, PASSWORD)
    else:
        bot.send_message(message.chat.id, "Я тебя не понял...")


@bot.message_handler(commands=['random'])
def random_message(message):
    if random.randint(1, 10) == 1:
        bot.send_message(message.chat.id, FLAG6)


@bot.message_handler(content_types=['sticker'])
def check_sticker(message):
    if message.sticker.set_name in ['videocatt_by_fStikBot']:
        bot.send_message(message.chat.id, FLAG7)
    else:
        bot.send_message(message.chat.id, "😿 Это не тот стикер!")


bot.polling(none_stop=True)

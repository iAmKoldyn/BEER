import random
import telebot
import time
from telebot import types
import os
import json
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.environ.get('TOKEN'))
@bot.message_handler(commands=['start'])
def starting(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('ℹ️ info')
    item2 = types.KeyboardButton('🍾 Алкогольное')
    item3 = types.KeyboardButton('🧋 Безалкогольное')
    item4 = types.KeyboardButton('🍫 Чоколадки')
    item5 = types.KeyboardButton('⚡️tip of the day')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Ну что {0.first_name}, пивка для рывка?)'.format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'ℹ️ info':
            bot.send_message(message.chat.id, 'Ты промазал, кнопка подборки жидкого золота находится правее')
        elif message.text == '🍾 Алкогольное':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🍺 beer')
            item2 = types.KeyboardButton('🧃 sidr')
            back = types.KeyboardButton('⬅️ назад')

            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, '🍾 Алкогольное', reply_markup=markup)

        elif message.text == '🧋 Безалкогольное':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🧉 Напитки')
            item2 = types.KeyboardButton('🥤 Снимает дебафы от пива')
            item3 = types.KeyboardButton('☕️ Кофе')
            item4 = types.KeyboardButton('Стикер')
            back = types.KeyboardButton('⬅️ назад')

            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, 'Для девочек)', reply_markup=markup)



        elif message.text == '⚡️tip of the day':
            bot.send_message(message.chat.id, '\nСпасибо, что доверились моему выбору)\n')
            json_data = open(r'data/beer.json', encoding='utf')
            data = json.load(json_data)
            key = list(data.keys())[random.randint(0,len(list(data.keys())))]
            value = data[key]
            beer_markup = types.InlineKeyboardMarkup(row_width=2)
            beer_markup.add(types.InlineKeyboardButton('На сайт', url=value['beer_hrefs']),
                            types.InlineKeyboardButton('Назад', callback_data='back_menu'),
                            )
            bot.send_photo(message.chat.id, value['beer_image'],
                           caption=f'🔸*{key.split(" - ")[0]}*\n\n🔸Количество: *{key.split(" - ")[1]}*\n\n🔸Цена: *{value["beer_price"]}* ₽',
                           reply_markup=beer_markup, parse_mode="Markdown")


        elif message.text == '⬅️ назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('ℹ️ info')
            item2 = types.KeyboardButton('🍾 Алкогольное')
            item3 = types.KeyboardButton('🧋 Безалкогольное')
            item4 = types.KeyboardButton('🍫 Чоколадки')
            item5 = types.KeyboardButton('⚡️tip of the day')

            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, '⬅️ назад', reply_markup=markup)




    elif call.data.split('_')[0] == 'back' and call.data.split('_')[1] == 'menu':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('ℹ️ info')
        item2 = types.KeyboardButton('🍾 Алкогольное')
        item3 = types.KeyboardButton('🧋 Безалкогольное')
        item4 = types.KeyboardButton('🍫 Чоколадки')
        item5 = types.KeyboardButton('⚡️tip of the day')

        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(call.message.chat.id,'Что выберешь на этот раз?',reply_markup=markup)


bot.polling(none_stop=True)
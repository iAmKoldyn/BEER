import random 
import telebot 
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.environ.get('TOKEN'))

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('ℹ️ info')
    item2 = types.KeyboardButton('🍾 Алкогольное')
    item3 = types.KeyboardButton('🧋 Безалкогольное')
    item4 = types.KeyboardButton('🍫 Чоколадки') 
    item5 = types.KeyboardButton('⚡️tip of the day')
   

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Ну что {0.first_name}, пивка для рывка?)'.format(message.from_user), reply_markup=markup)   
  

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'ℹ️ info':
            bot.send_message(message.chat.id, 'Ты промазал, кнопка подборки жидкого золота находится правее')

        elif message.text == '🍾 Алкогольное':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🍺 bear')
            if message.text == '🍺 bear':
                bot.send_message(message.chat.id,'🍾 Алкогольное', reply_markup=markup)                
                
            item2 = types.KeyboardButton('🧃 cidr')
            back = types.KeyboardButton('⬅️ назад')

            markup.add(item1, item2, back)
            
            bot.send_message(message.chat.id,'🍾 Алкогольное', reply_markup=markup)

        elif message.text == '🧋 Безалкогольное':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🧉 Напитки')
            item2 = types.KeyboardButton('🥤 Снимает дебафы от пива')
            item3 = types.KeyboardButton('☕️ Кофе')
            item4 = types.KeyboardButton('Стикер')
            back = types.KeyboardButton('⬅️ назад')

            markup.add(item1, item2, item3, item4, back)
                
            bot.send_message(message.chat.id,'Для девочек)', reply_markup=markup)

        elif message.text == '🍫 Чоколадки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,'Подборочка чоколадок:', reply_markup=markup)
    


        elif message.text == '⚡️tip of the day':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,'\nСпасибо, что доверились нашему выбору)\n', reply_markup=markup)


        elif message.text == '⬅️ назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('ℹ️ info')
            item2 = types.KeyboardButton('🍾 Алкогольное')
            item3 = types.KeyboardButton('🧋 Безалкогольное')
            item4 = types.KeyboardButton('🍫 Чоколадки') 
            item5 = types.KeyboardButton('⚡️tip of the day')

            markup.add(item1, item2, item3, item4, item5)
    
            bot.send_message(message.chat.id, '⬅️ назад', reply_markup=markup)


        elif message.text == 'Стикер':
            stick = open('static/sticker.webp', 'rb')
            bot.send_sticker(message.chat.id, stick)

bot.polling(none_stop=True)
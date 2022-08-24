import telebot
from telebot import types
from owm import show_data

bot=telebot.TeleBot("TG-Bot token") 

cities = ['Пермь']
btn_content = ['⛅ Погода', '🔙 Назад', '📍 Текущее местоположение']

@bot.message_handler(commands = ['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn_weather = types.KeyboardButton(btn_content[0])
    markup.add(btn_weather)
    bot.send_message(message.chat.id, text = "✌️ Привет, {0.first_name}!".format(message.from_user), reply_markup = markup)
    
@bot.message_handler(commands = ['help'])
def help_message(message):
    bot.send_message(message.chat.id,"🤖 Я бот CryppSe. На данный момент я имею мало полезного функционала, но мой разработчик уже исправляет это.")
    
@bot.message_handler(content_types = ['text'])
def text_message(message):
    if(message.text == btn_content[0]):
        weather(message)

    elif(message.text == btn_content[1]):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn_weather = types.KeyboardButton(btn_content[0])
        markup.add(btn_weather)
        bot.send_message(message.chat.id, text="Выбрите раздел", reply_markup = markup)
    else:
        show_weather(message)

#Current geo-position        
@bot.message_handler(content_types = ['location'])
def handle_loc(message):
    bot.send_message(message.chat.id, show_data(message.location))

def weather(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn_geo = types.KeyboardButton(btn_content[2], request_location = True)
    markup.row(cities[0])
    markup.row(btn_geo, btn_content[1])
    bot.send_message(message.chat.id, text = "Введите название города или выберите из списка", reply_markup = markup)
    
def show_weather(message):
    bot.send_message(message.chat.id, show_data(message.text))

bot.polling()








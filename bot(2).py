import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)




#Кнопки URL
@bot.message_handler(commands=['news'])
def url(message):
	markup = types.InlineKeyboardMarkup()
	btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='https://www.mr-info.ru')
	markup.add(btn_my_site)
	bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)

#Text
@bot.message_handler(content_types=["text"])
def handle_text(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Здраствуйте, чем могу вам помочь?")

	elif message.text == "Как дела?" or message.text == "Как ты?":
		bot.send_message(message.from_user.id, "Отлично! А вы?")

	else:
		bot.send_message(message.from_user.id, "Извините, я вас не понял.")

# RUN
bot.polling(none_stop=True)
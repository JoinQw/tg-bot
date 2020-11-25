import telebot
from sqlighter import SQLighter



# Token
bot = telebot.TeleBot('1483806836:AAGat6NFaQUTq_Xxd9fCqagr-poHDwpz1Vo')

# Connect db
db = SQLighter('db.db')

# Keyboard at the start
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Подписаться', 'Нет, спасибо.')


# Start and Welcome
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                    'Здраствуйте!, вы нажали на стартовую команду. \n Нежелаете подписаться на новостную рассылку?',
                     reply_markup=keyboard1)

    # Subscribe/unsubscribe news
    @bot.message_handler(commands=['subscribe'])
    def subscribe_message(message):
        bot.send_message(message.chat.id, 'Вы подписались на рассылку! \n В скором времени вы будете получать уведомления об новостях;-)')
    @bot.message_handler(commands=['unsubscribe'])
    def unsubscribe_message(message):
        bot.send_message(message.chat.id, 'Вы отписались от рассылки:с \n Я буду скучать по вам.Возращайтесь по скорее')


# Stickers


# Launch
bot.polling()

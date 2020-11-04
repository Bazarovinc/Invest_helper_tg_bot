import telebot
import config as con
from functions.currency import currency

bot = telebot.TeleBot(con.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id, "Hello, I'm your personal Invest helper! Use /help to get more"
                         "information.")


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.from_user.id, con.help_message)


@bot.message_handler(commands=['currency'])
def currency_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('USD', callback_data="USD"),
        telebot.types.InlineKeyboardButton('EUR', callback_data="EUR")
    )
    bot.send_message(message.from_user.id, 'Click on the currency:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    bot.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data)


def send_exchange_result(message, ex_code):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, currency(str(ex_code)))


bot.polling(none_stop=True, interval=0)

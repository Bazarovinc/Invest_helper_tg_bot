import telebot
import config as con

bot = telebot.TeleBot(con.TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Hello, I'm your personal Invest helper!")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, con.help_message)
    elif message.text == '/currency':
        pass
    else:
        bot.send_message(message.from_user.id, "Can't understand you, use /help to get more information.")


bot.polling(none_stop=True, interval=0)
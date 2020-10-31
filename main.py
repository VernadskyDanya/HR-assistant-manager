import telebot
import passwords
from telebot import types
bot = telebot.TeleBot(passwords.key)

def start(message_chat_id):
    button1 = types.InlineKeyboardButton(text="У меня вопрос по рекрутменту", callback_data="Recrut")
    button2 = types.InlineKeyboardButton(text="У меня вопрос по обучению", callback_data="Study")
    button3 = types.InlineKeyboardButton(text="У меня вопрос по адаптации", callback_data="Adaptation")
    button4 = types.InlineKeyboardButton(text="У меня вопрос по кадровому резерву", callback_data="PersReserve")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    bot.send_message(message_chat_id, "Чем тебе помочь?\n", reply_markup=markup)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name)
                 + ", это твой личный HR помощник руководителя! Я всегда готов помочь тебе с вопросами.\n"
                   "Ты всегда можешь вернуться в меню командой /start")
    start(message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "start":
        start(call.message.chat.id)

    if call.data =="coffee":
        from functions import coffee
        coffee(call.message.chat.id, bot, types)


bot.polling(none_stop=False, interval=0, timeout=20)
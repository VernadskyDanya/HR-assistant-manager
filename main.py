import telebot
import passwords
from telebot import types
bot = telebot.TeleBot(passwords.key)

"""
import os
from flask import Flask, request
import logging
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
server = Flask(__name__)
os.environ['FLASK_ENV'] = 'development'


@server.route('/' + passwords.key, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
"""


def start(message_chat_id):
    button1 = types.InlineKeyboardButton(text="👨🏼‍⚖️У меня вопрос по рекрутменту", callback_data="recrut")
    button2 = types.InlineKeyboardButton(text="📘 У меня вопрос по обучению", callback_data="study")
    button3 = types.InlineKeyboardButton(text="🐧 У меня вопрос по адаптации", callback_data="adaptation")
    button4 = types.InlineKeyboardButton(text="👩🏻‍🔬 У меня вопрос по кадровому резерву",
                                         callback_data="persReserve")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    bot.send_message(message_chat_id, "Чем вам помочь?\n", reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name) +
                     ", это ваш личный HR помощник руководителя! Я всегда готов вам помочь с вопросами.\n"
                     "Ты всегда можешь вернуться в меню командой /start")
    start(message.chat.id)


from branches import adaptBranch
from branches import persResBranch
from branches import recrutBranch
from branches import studyBranch

# Словарь для callback_query_handler
FUNCTIONS = dict(
                    # Ветка Вопрос по рекрутменту
                    recrut=recrutBranch.recrut, vacation=recrutBranch.vacation, budget=recrutBranch.budget,
                    inSearch=recrutBranch.inSearch, outSearch=recrutBranch.outSearch, rules=recrutBranch.rules,
                    acceptIn=recrutBranch.acceptIn, wantOpenIn=recrutBranch.wantOpenIn, fetchIn=recrutBranch.fetchIn,
                    fetchOut=recrutBranch.fetchOut, acceptOut=recrutBranch.acceptOut,
                    wantOpenOut=recrutBranch.wantOpenOut,
                    # Ветка Вопрос по обучению
                    study=studyBranch.study, howToLearn=studyBranch.howToLearn, iKnow=studyBranch.iKnow,
                    helpProgram=studyBranch.helpProgram, restriction=studyBranch.restriction,
                    # Ветка Вопрос по адаптации
                    adaptation=adaptBranch.adaptation, whatToDo=adaptBranch.whatToDO, myRole=adaptBranch.myRole,
                    taskToCheck=adaptBranch.taskToCheck, baddy=adaptBranch.baddy, mentor=adaptBranch.mentor,
                    reminders=adaptBranch.reminders,
                    # Ветка Вопрос по кадровому резерву
                    persReserve=persResBranch.persRes
)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "start":
        start(call.message.chat.id)
    else:
        FUNCTIONS[call.data](call.message.chat.id, bot)

"""
#bot.polling(none_stop=False, interval=0, timeout=20)
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://hr-assistant-manager.herokuapp.com/' + passwords.key)
    return "!", 200

server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
"""
bot.polling(none_stop=False, interval=0, timeout=20)
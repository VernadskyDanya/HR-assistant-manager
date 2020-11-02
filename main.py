import os

import telebot
import passwords
from telebot import types
bot = telebot.TeleBot(passwords.key)

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


def start(message_chat_id):
    button1 = types.InlineKeyboardButton(text="👨🏼‍⚖️У меня вопрос по рекрутменту", callback_data="recrut")
    button2 = types.InlineKeyboardButton(text="📘 У меня вопрос по обучению", callback_data="study")
    button3 = types.InlineKeyboardButton(text="🐧 У меня вопрос по адаптации", callback_data="adaptation")
    button4 = types.InlineKeyboardButton(text="👩🏻‍🔬 У меня вопрос по кадровому резерву", callback_data="persReserve")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    bot.send_message(message_chat_id, "Чем тебе помочь?\n", reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name)
                 + ", это твой личный HR помощник руководителя! Я всегда готов помочь тебе с вопросами.\n"
                   "Ты всегда можешь вернуться в меню командой /start")
    start(message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "start":
        start(call.message.chat.id)

        """Ветка Вопрос по рекрутменту"""

    if call.data == "recrut":
        from recrutBranch import recrut
        recrut(call.message.chat.id, bot)
    if call.data == "vacation":
        from recrutBranch import vacation
        vacation(call.message.chat.id, bot)
    if call.data == "budget":
        from recrutBranch import budget
        budget(call.message.chat.id, bot)
    if call.data == "inSearch":
        from recrutBranch import inSearch
        inSearch(call.message.chat.id, bot)
    if call.data == "outSearch":
        from recrutBranch import outSearch
        outSearch(call.message.chat.id, bot)
    if call.data == "rules":
        from recrutBranch import rules
        rules(call.message.chat.id, bot)
    if call.data == "acceptIn":
        from recrutBranch import acceptIn
        acceptIn(call.message.chat.id, bot)
    if call.data == "wantOpenIn":
        from recrutBranch import wantOpenIn
        wantOpenIn(call.message.chat.id, bot)
    if call.data == "fetchIn":
        from recrutBranch import fetchIn
        fetchIn(call.message.chat.id, bot)
    if call.data == "fetchOut":
        from recrutBranch import fetchOut
        fetchOut(call.message.chat.id, bot)
    if call.data == "acceptOut":
        from recrutBranch import acceptOut
        acceptOut(call.message.chat.id, bot)
    if call.data == "wantOpenOut":
        from recrutBranch import wantOpenOut
        wantOpenOut(call.message.chat.id, bot)

        """Ветка Вопрос по обучению"""

    if call.data == "study":
        from studyBranch import study
        study(call.message.chat.id, bot)
    if call.data == "howToLearn":
        from studyBranch import howToLearn
        howToLearn(call.message.chat.id, bot)
    if call.data == "iKnow":
        from studyBranch import iKnow
        iKnow(call.message.chat.id, bot)
    if call.data == "helpProgram":
        from studyBranch import helpProgram
        helpProgram(call.message.chat.id, bot)
    if call.data == "restriction":
        from studyBranch import restriction
        restriction(call.message.chat.id, bot)

        """Ветка Вопрос по адаптации"""

    if call.data == "adaptation":
        from adaptBranch import adaptation
        adaptation(call.message.chat.id, bot)
    if call.data == "whatToDo":
        from adaptBranch import whatToDO
        whatToDO(call.message.chat.id, bot)
    if call.data == "myRole":
        from adaptBranch import myRole
        myRole(call.message.chat.id, bot)
    if call.data == "taskToCheck":
        from adaptBranch import taskToCheck
        taskToCheck(call.message.chat.id, bot)
    if call.data == "baddy":
        from adaptBranch import baddy
        baddy(call.message.chat.id, bot)
    if call.data == "mentor":
        from adaptBranch import mentor
        mentor(call.message.chat.id, bot)
    if call.data == "reminders":
        from adaptBranch import reminders
        reminders(call.message.chat.id, bot)

        """Ветка Вопрос по кадровому резерву"""

    if call.data == "persReserve":
        from persResBranch import persRes
        persRes(call.message.chat.id, bot)


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://hr-assistant-manager.herokuapp.com/' + passwords.key)
    return "!", 200


server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
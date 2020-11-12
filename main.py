import telebot
import passwords
from telebot import types
import time
bot = telebot.TeleBot(passwords.key)


# Процесс для отправки напоминаний
def run_reminder():
    print("Run_reminder has started")
    from sql_alchemy import send_reminder
    while True:
        try:
            send_reminder(bot)
            time.sleep(86400)  # 24 часа
        except Exception as ex:
            import logging
            logging.critical(ex)
            bot.send_message(204181538, "Произошла ошибка отправки напоминания")
            break


# Процесс для работы меню
def run_menu():
    print("Run_menu has started")

    import os
    from flask import Flask, request
    import logging
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)
    server = Flask(__name__)
    os.environ['FLASK_ENV'] = 'development'
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

    @server.route('/' + passwords.key, methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "?", 200

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
        bot.send_message(message_chat_id, "Чем тебе помочь?\n", reply_markup=markup)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name) +
                         ", это твой личный HR помощник руководителя! Я всегда готов помочь тебе с вопросами.\n"
                         "Ты всегда можешь вернуться в меню командой /start")
        start(message.chat.id)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "start":
            start(call.message.chat.id)

        """Ветка Вопрос по рекрутменту"""

        if call.data == "recrut":
            from branches.recrutBranch import recrut
            recrut(call.message.chat.id, bot)
        if call.data == "vacation":
            from branches.recrutBranch import vacation
            vacation(call.message.chat.id, bot)
        if call.data == "budget":
            from branches.recrutBranch import budget
            budget(call.message.chat.id, bot)
        if call.data == "inSearch":
            from branches.recrutBranch import inSearch
            inSearch(call.message.chat.id, bot)
        if call.data == "outSearch":
            from branches.recrutBranch import outSearch
            outSearch(call.message.chat.id, bot)
        if call.data == "rules":
            from branches.recrutBranch import rules
            rules(call.message.chat.id, bot)
        if call.data == "acceptIn":
            from branches.recrutBranch import acceptIn
            acceptIn(call.message.chat.id, bot)
        if call.data == "wantOpenIn":
            from branches.recrutBranch import wantOpenIn
            wantOpenIn(call.message.chat.id, bot)
        if call.data == "fetchIn":
            from branches.recrutBranch import fetchIn
            fetchIn(call.message.chat.id, bot)
        if call.data == "fetchOut":
            from branches.recrutBranch import fetchOut
            fetchOut(call.message.chat.id, bot)
        if call.data == "acceptOut":
            from branches.recrutBranch import acceptOut
            acceptOut(call.message.chat.id, bot)
        if call.data == "wantOpenOut":
            from branches.recrutBranch import wantOpenOut
            wantOpenOut(call.message.chat.id, bot)

        """Ветка Вопрос по обучению"""

        if call.data == "study":
            from branches.studyBranch import study
            study(call.message.chat.id, bot)
        if call.data == "howToLearn":
            from branches.studyBranch import howToLearn
            howToLearn(call.message.chat.id, bot)
        if call.data == "iKnow":
            from branches.studyBranch import iKnow
            iKnow(call.message.chat.id, bot)
        if call.data == "helpProgram":
            from branches.studyBranch import helpProgram
            helpProgram(call.message.chat.id, bot)
        if call.data == "restriction":
            from branches.studyBranch import restriction
            restriction(call.message.chat.id, bot)

        """Ветка Вопрос по адаптации"""

        if call.data == "adaptation":
            from branches.adaptBranch import adaptation
            adaptation(call.message.chat.id, bot)
        if call.data == "whatToDo":
            from branches.adaptBranch import whatToDO
            whatToDO(call.message.chat.id, bot)
        if call.data == "myRole":
            from branches.adaptBranch import myRole
            myRole(call.message.chat.id, bot)
        if call.data == "taskToCheck":
            from branches.adaptBranch import taskToCheck
            taskToCheck(call.message.chat.id, bot)
        if call.data == "baddy":
            from branches.adaptBranch import baddy
            baddy(call.message.chat.id, bot)
        if call.data == "mentor":
            from branches.adaptBranch import mentor
            mentor(call.message.chat.id, bot)
        if call.data == "reminders":
            from branches.adaptBranch import reminders
            reminders(call.message.chat.id, bot)

        """Ветка Вопрос по кадровому резерву"""

        if call.data == "persReserve":
            from branches.persResBranch import persRes
            persRes(call.message.chat.id, bot)

    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url='https://telegrambot151.herokuapp.com/' + passwords.key)
        return "!", 200

    #bot.polling(none_stop=False, interval=0, timeout=20)

    logger.critical("Exiting mainMenu thread!?!?...")

# Создать процессы
import multiprocessing as mp
import logging
mp.log_to_stderr()
logger = mp.get_logger()
logger.setLevel(logging.INFO)
if __name__ == '__main__':
    bot.remove_webhook()
    proc_rem = mp.Process(target=run_reminder, daemon= False)
    proc_menu = mp.Process(target=run_menu, daemon = False)
    proc_rem.start()
    proc_menu.start()

logger.info("Exiting the Program!")


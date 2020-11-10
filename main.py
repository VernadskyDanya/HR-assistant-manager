import telebot
import passwords
from telebot import types
import threading
import time
bot = telebot.TeleBot(passwords.key)


# Поток для отправки напоминаний
class ThreadTimeToCheck(threading.Thread):
    def __init__(self):
            threading.Thread.__init__(self)

    def run(self):
        print("ThreadTimeToCheckHasStarted...")
        from sql_alchemy import send_reminder
        while True:
            try:
                send_reminder(bot)
                time.sleep(86400)  # 24 часа
            except Exception as ex:
                import logging
                logging.critical(ex)
                bot.send_message(204181538, "Произошла ошибка отправка сообщений, вам стоит обратиться к @danya04"
                                                  " и к @tatyanagolovina1")
                break


# Поток для работы меню
class MainMenu(threading.Thread):
   def __init__(self):
       threading.Thread.__init__(self)
   def run(self):
       print("Starting mainMenu thread")

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

       bot.polling(none_stop=False, interval=0, timeout=20)

       print("Exiting mainMenu thread!?!?......")

# Создать треды


thread1 = ThreadTimeToCheck()
thread2 = MainMenu()

# Запустить треды
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Exiting the Program!!!")


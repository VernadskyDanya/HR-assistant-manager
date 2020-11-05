import telebot
import passwords
from telebot import types
import threading
import time
bot = telebot.TeleBot(passwords.key)


# Поток для отправки напоминаний
class threadTimeToCheck(threading.Thread):
    def __init__(self):
            threading.Thread.__init__(self)

    def run(self):
           print("Starting TimeToCheck thread")
           while True:
               print("threadTimeToCheck is working! :)")
               time.sleep(3)
           print("Exiting ")


# Поток для работы меню
class mainMenu(threading.Thread):
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

       bot.polling(none_stop=False, interval=0, timeout=20)

       print("Exiting mainMenu thread!?!?......")

# Создать треды


thread1 = threadTimeToCheck()
thread2 = mainMenu()

# Запустить треды
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Exiting the Program!!!")


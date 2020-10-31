"""Ветка Вопрос по адаптации"""

from telebot import types


def adaptation(message_chat_id, bot):
    button1 = types.InlineKeyboardButton(text="У меня выходит новый сотрудник - что сделать?",
                                         callback_data="whatToDo")
    button2 = types.InlineKeyboardButton(text="Какова моя роль в процессе адаптации сотрудника",
                                         callback_data="myRole")
    button5 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button5)
    bot.send_message(message_chat_id, "Выбери вопрос по адаптации:", reply_markup=markup)


def whatToDO(message_chat_id, bot):
    button1 = types.InlineKeyboardButton(text="Составить задание на испытательный срок",
                                         callback_data="taskToCheck")
    button2 = types.InlineKeyboardButton(text="Назначить Бадди",
                                         callback_data="baddy")
    button3 = types.InlineKeyboardButton(text="Назначить наставника",
                                         callback_data="mentor")
    button4 = types.InlineKeyboardButton(text="Настроить напоминания",
                                         callback_data="reminders")
    button5 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="adaptation")
    button6 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    markup.row(button6)
    bot.send_message(message_chat_id, "Выбери вопрос по адаптации:", reply_markup=markup)


def taskToCheck(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="adaptation")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "",
                     parse_mode = 'HTML', reply_markup=markup)


def baddy(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="adaptation")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "",
                     parse_mode = 'HTML', reply_markup=markup)


def mentor(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="adaptation")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "",
                     parse_mode = 'HTML', reply_markup=markup)


def reminders(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="adaptation")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "In progress",
                     parse_mode = 'HTML', reply_markup=markup)


def myRole(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="adaptation")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "",
                     parse_mode = 'HTML', reply_markup=markup)
"""Ветка Вопрос по обучению"""

from telebot import types


def study(message_chat_id, bot):
    button1 = types.InlineKeyboardButton(text="Как формируется потребность в обучении",
                                         callback_data="howToLearn")
    button2 = types.InlineKeyboardButton(text="Я знаю, чему хочу обучиться/обучить сотрудника", callback_data="iKnow")
    button3 = types.InlineKeyboardButton(text="Помощь в выборе программы", callback_data="helpProgram")
    button4 = types.InlineKeyboardButton(text="Какие есть ограничения по обучению?", callback_data="restriction")
    button5 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Выбери вопрос по обучению", reply_markup=markup)


def howToLearn(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="study")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Потребность в обучении формируется <b>совместно "
                                      "с HR-партнером в конце предшествующего года</b>. При"
                                      " этом вы можете:\nобучить чему-то все подразделение\n"
                                      "направить на точечное обучение конкретного сотрудника\n"
                                      "Ознакомиться с програмами корпортаивного университета и "
                                      "одобренных КУ провайдеров можно в разделе: <b>База знаний - "
                                      "Портал обучения - Навигатор образовательных продуктов</b>",
                     parse_mode = 'HTML', reply_markup=markup)


def iKnow(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="study")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Если вы выбрали для себя или своего сотрудника <b>конкретную "
                                      "программу</b>, направьте данную информацию своему  HR-партнер для"
                                      " обсуждения возможностей бюджета и запуска на оплату",
                     parse_mode = 'HTML', reply_markup=markup)


def helpProgram(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="study")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Если <b>вы знаете, в каком направлении необходимо обучение</b>, но "
                                      "вам необходим <b>подбор программы</b> - обратитесь за консультацией "
                                      "к своему HR-партнеру. Обучение будет организовано по факту выбора программы",
                     parse_mode = 'HTML', reply_markup=markup)


def restriction(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="study")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Дорогостоящее обучение (<b>от 350 до 500 тыс</b>) - "
                                      "требует согласования со стороны"
                                      " ДД и КУ и ЗГД БОВ. \nДорогостоящее обучение <b>от 500 тыс</b> - требует те же "
                                      "согласований, кроме того, по правилам компании, <b>оплачивается на 30% "
                                      "самим сотрудником</b>. \nВ компании запрещено обучение, предполагающее "
                                      "выезд за границу",
                     parse_mode = 'HTML', reply_markup=markup)

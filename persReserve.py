"""Ветка Вопрос по кадровому резерву"""
from telebot import types


def baddy(message_chat_id, bot):
    button1 = types.InlineKeyboardButton(text="Бот Помощник Руководителя ",
                                         url="https://t.me/Personnel_helpbot")
    button2 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    bot.send_message(message_chat_id, "Для этого перейди в бот",
                     parse_mode = 'HTML', reply_markup=markup)
# Скрипт для отправки напоминаний
import telebot
import passwords
bot = telebot.TeleBot(passwords.key)
from sql_alchemy import send_reminder

try:
    send_reminder(bot)
    bot.send_message(204181538, "Отправка напоминания!:)")
except Exception as ex:
    import logging
    logging.critical(ex)
    bot.send_message(204181538, "Произошла ошибка отправки напоминания")
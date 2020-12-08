# Скрипт для отправки напоминаний
import telebot
import passwords
bot = telebot.TeleBot(passwords.key)

try:
    # ПОДКЛЮЧАЕМСЯ К MONGOCLIENT
    import pymongo
    import passwords
    client = pymongo.MongoClient(passwords.mongodb_key)
    # ПОЛУЧАЕМ БАЗУ ДАННЫХ
    db = client['GN-reminders']
    # ПОЛУЧАЕМ КОЛЛЕКЦИЮ
    collection = db['Reminders-Adaptation']

    import time
    from datetime import date

    current_time = date(time.localtime()[0], time.localtime()[1], time.localtime()[2])  # Текущая дата
    from datetime import timedelta

    time_delta1 = timedelta(-30)
    time_delta2 = timedelta(-60)
    time_delta3 = timedelta(-74)
    for instance in db.posts.find({}):
        s = instance['time_for_db'].split('-')  # Получаем список из трех элементов
        time_from_db = date(int(s[0]), int(s[1]), int(s[2])) # Переводим из типа string к типу date
        if (time_from_db - current_time) == time_delta1:
            from reminder_messages import func_time_delta1
            func_time_delta1(instance['message_chat_id'], instance['beginner_name'], bot)
            continue
        if (time_from_db - current_time) == time_delta2:
            from reminder_messages import func_time_delta2
            func_time_delta2(instance['message_chat_id'], instance['beginner_name'], bot)
            continue
        if (time_from_db - current_time) == time_delta3:
            from reminder_messages import func_time_delta3
            func_time_delta3(instance['message_chat_id'], instance['beginner_name'], bot)
            continue
except Exception as ex:
    import logging
    logging.critical(ex)
    bot.send_message(204181538, "Произошла ошибка отправки напоминания")
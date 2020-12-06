"""Ветка Вопрос по адаптации"""

from telebot import types


def adaptation(message_chat_id, bot):
    button1 = types.InlineKeyboardButton(text="🆕 У меня выходит новый сотрудник - что сделать?",
                                         callback_data="whatToDo")
    button2 = types.InlineKeyboardButton(text="🌾 Какова моя роль в процессе адаптации сотрудника",
                                         callback_data="myRole")
    button5 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button5)
    bot.send_message(message_chat_id, "Выберите вопрос по адаптации:", reply_markup=markup)


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
    markup.add(button5, button6)
    bot.send_message(message_chat_id, "Выберите вопрос по выходу нового сотрудника:", reply_markup=markup)


def taskToCheck(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="whatToDo")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.add(button4, button5)
    bot.send_message(message_chat_id, "В задании на испытательный срок необходимо отразить <b>основные "
                                      "задачи на первые 3 месяца</b> с конкретными результатми и сроками. "
                                      "Важно ознакомить новичка с заданием в первую неделю работы "
                                      "(под подпись), ответить на его вопросы, "
                                      "<b>фиксировать результаты выполняемых задач</b>",
                     parse_mode = 'HTML', reply_markup=markup)


def baddy(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="whatToDo")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.add(button4, button5)
    bot.send_message(message_chat_id, "<b>Бадди</b> помогает привыкнуть к новому рабочему месту и решить "
                                      "все неформальные вопросы, а также создать дружелюбную атмосферу"
                                      "\nБадди сориентирует нового сотрудника  по офису (проведет экскурсию,"
                                      " покажет, где расположено все необходимое для работы и отдыха), "
                                      "подскажет, какую интересную информацию можно найти на корпоративном "
                                      "портале и как на портал попасть. Бадди и Новый сотрудник вместе "
                                      "пообедают/перекусят/попьют кофе, чтобы в спокойной обстановке "
                                      "обсудить неформальные вопросы",
                     parse_mode = 'HTML', reply_markup=markup)


def mentor(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="whatToDo")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.add(button4, button5)
    bot.send_message(message_chat_id, "<b>Наставник</b> помогает новичку почувствовать себя «своим» "
                                      "- знакомит с компанией и командой Новичок не тратит время "
                                      "на поиск структурной, контактной и прочей внутренней "
                                      "информации о компании – всю информацию предоставляет Наставник"
                                      "\nТакже наставник помогает быстрее и качественнее погрузиться в рабочие задачи",
                     parse_mode = 'HTML', reply_markup=markup)


def reminders(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="whatToDo")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.add(button4, button5)
    bot.send_message(message_chat_id, "Представьтесь в формате Фамилия Имя Отчество:",
                     parse_mode = 'HTML', reply_markup=markup)

    @bot.message_handler(content_types=['text'])    # Инициализация руководителя и нового сотрудника
    def process_manager(message):  # Инициализация руководителя
        s = message.text.split()
        length = len(s)  # Смотрим количество слов, должно быть три (ФИО)
        if length == 3:
            leader_name = s[0] + " " + s[1] + " " + s[2] # Собираем обратно строчку
            bot.reply_to(message, "Как зовут вашего нового сотрудника (в формате Фамилия Имя Отчество):")
            return bot.register_next_step_handler(message, process_beginner, leader_name)
        else:
            bot.reply_to(message, "Упс, я вас не понимаю, проверьте написание "
                                  "ФИО или воспользуйтесь кнопками для меню")

    def process_beginner(message, leader_name):     # Инициализация нового сотрудника
        s = message.text.split()
        length = len(s)  # Смотрим количество слов, должно быть три (ФИО)
        if length == 3:
            beginner_name = message.text
            bot.reply_to(message, "Когда начал работать новый сотрудник?\n"
                                  "Пожалуйста, напишите дату в формате 2020 09 28")
            return bot.register_next_step_handler(message, process_time, leader_name, beginner_name)
        else:
            bot.reply_to(message, "Упс, я вас не понимаю.\n"
                                  "1. Проверьте написание ФИО и начните заново c ввода имени руководителя\n"
                                  "2. Воспользуйтесь кнопками интерактивного меню")

    def process_time(message, leader_name, beginner_name):
        s = message.text.split()
        # Создаём время для БД
        from datetime import date
        time_for_db = str(date(int(s[0]), int(s[1]), int(s[2])))
        try:
            from db_operations import add_request
            add_request(message_chat_id, leader_name, beginner_name, time_for_db)
            return reminders_is_ok(message.chat.id, bot)
        except Exception as ex:
            import logging
            logging.error(ex)
            bot.send_message(message_chat_id, "Произошла ошибка, вам стоит обратиться к @danya04"
                                              " и к @tatyanagolovina1",
                             parse_mode='HTML', reply_markup=markup)


def reminders_is_ok(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="whatToDo")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.add(button4, button5)
    bot.send_message(message_chat_id, "Поздравляем вас с выходом нового сотрудника! Для того, чтобы процесс адаптации "
                                      "новичка был максимально быстрым и комфортным в течение первой недели вам "
                                      "необходимо:\n"
                                      "1. Назначить наставника\n"
                                      "2. Назначить бадди\n"
                                      "3. Подготовить и ознакомить под подпись с заданием на испытательный срок\n\n"
                                      "Я буду присылать вам напоминания о точках проверки процесса адаптации\n"
                                      "Если у вас будут оставаться вопросы, пожалуйста, обратитесь с HR-партнеру",
                     parse_mode='HTML', reply_markup=markup)


def myRole(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="adaptation")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.add(button4, button5)
    bot.send_message(message_chat_id, "<b>Адаптация</b> –  важный и обоюдный процесс, вы можете повлиять "
                                      "на уровень приверженности, вовлеченности и лояльности сотрудника "
                                      "уже с первых дней. Для любого сотрудника важно <b>участие руководителя</b> "
                                      "в его профессиональной жизни\n<b>Важно на первых этапах</b>:\nМониторить "
                                      "качество работы сотрудника, отслеживать задание на испытательный срок"
                                      "\nОтвечать на сложные вопросы\nПовышать вовлеченность сотрудника"
                     ,parse_mode = 'HTML', reply_markup=markup)
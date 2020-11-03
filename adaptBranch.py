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
    markup.add(button5, button6)
    bot.send_message(message_chat_id, "Выбери вопрос по выходу нового сотрудника:", reply_markup=markup)


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
                                      "все неформальные вопросы, а также создать дружелюбную атмосферу."
                                      "\nБадди сориентирует нового сотрудника  по офису (проведет экскурсию,"
                                      " покажет, где расположено все необходимое для работы и отдыха), "
                                      "подскажет, какую интересную информацию можно найти на корпоративном "
                                      "портале и как на портал попасть. Бадди и Новый сотрудник вместе "
                                      "пообедают/перекусят/попьют кофе, чтобы в спокойной обстановке "
                                      "обсудить неформальные вопросы"
,
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
    bot.send_message(message_chat_id, "Представьтесь в формате Фамилия Имя Отчество",
                     parse_mode = 'HTML', reply_markup=markup)

    @bot.message_handler(content_types=['text'])    # Инициализация куратора и нового сотрудника
    def init(message):
        bot.send_message(message.chat.id, "cx")
        msg = bot.reply_to(message, 'Представьтесь в формате Фамилия Имя Отчество')
        bot.register_next_step_handler(msg, process_manager, bot)


def process_manager(message, bot):
    try:
        message = bot.reply_to(message, 'Вашего нового сотрудника зовут (в формате Фамилия Имя Отчество)')
    except Exception as e:
        bot.reply_to(message, 'oooops')


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
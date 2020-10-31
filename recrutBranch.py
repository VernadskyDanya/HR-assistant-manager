from telebot import types


def recrut(message_chat_id, bot):
    button1 = types.InlineKeyboardButton(text="Есть ли у меня вакансия",
                                         callback_data="vacation")
    button2 = types.InlineKeyboardButton(text="Как понять бюджет позиции", callback_data="budget")
    button3 = types.InlineKeyboardButton(text="Внутренний поиск",
                                         callback_data="inSearch")
    button4 = types.InlineKeyboardButton(text="Внешний поиск", callback_data="outSearch")
    button5 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Выбери вопрос по рекрутменту:", reply_markup=markup)


def vacation(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="recrut")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Проверить наличия вакансий в вашем подразделении можно, "
                                      "обратившись к <b>HR-партнеру</b>",
                     parse_mode = 'HTML', reply_markup=markup)


def budget(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="recrut")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Бюджет позиции и возможные предложения "
                                      "кандидату <b>вам подскажет HR-партнер</b>",
                     parse_mode = 'HTML', reply_markup=markup)


def inSearch(message_chat_id, bot):
    button1 = types.InlineKeyboardButton(text="Какие правила внутреннего перемещения?",
                                         callback_data="rules")
    button2 = types.InlineKeyboardButton(text="Хочу принять на работу сотрудника из периметра", callback_data="acceptIn")
    button3 = types.InlineKeyboardButton(text="Хочу открыть внутренний поиск",
                                         callback_data="wantOpenIn")
    button4 = types.InlineKeyboardButton(text="Подать заявку на поиск",
                                         callback_data="fetchIn")
    button5 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="recrut")
    button6 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    markup.row(button6)
    bot.send_message(message_chat_id, "Выбери вопрос по внутреннему поиску:", reply_markup=markup)


def rules(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="inSearch")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Для сотрудников, отработавших в текущей должности менее\n"
                                      "<b>1,5 лет</b> - ВС, ГС; \n<b>2 лет</b> - РН,НО; \n<b>3 лет</b> - НУ"
                                      "\nтребуется обязательное <b>письменное согласование руководителя</b>. "
                                      "\nРуководитель имеет право задержать сотрудника для отработки "
                                      "<b>на срок до 1,5 месяцев</b>.\nСотрудники из кадрового резерва и "
                                      "списка HiPo рассматриваются в первую очередь",
                     parse_mode = 'HTML', reply_markup=markup)


def acceptIn(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="inSearch")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Если вас заинтересовал конкретный сотрудник, вам необходимо, "
                                      "в первую очередь, направить <b>запрос на рассмотрение данного "
                                      "сотрудника его текущему руководителю</b>. Только после получения "
                                      "согласования возможно начинать комуникацию с самим сотрудником "
                                      "и с HR-партнером вашего подраделения на предмет "
                                      "согласования условий перехода",
                     parse_mode = 'HTML', reply_markup=markup)


def wantOpenIn(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="inSearch")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Если у вас есть или в ближайшее время открывается позиция, вам "
                                      "необходимо <b>описать требования и обязанности</b> в рамках позиции в "
                                      "любом удобном формате и направить данную информацию HR-партнеру",
                     parse_mode='HTML', reply_markup=markup)


def fetchIn(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="inSearch")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Когда-то тут будет бот по рекрутменту",
                     parse_mode = 'HTML', reply_markup=markup)


def outSearch(message_chat_id, bot):
    button1 = types.InlineKeyboardButton(text="Есть внешний кандидат, которого я хочу принять",
                                         callback_data="acceptOut")
    button2 = types.InlineKeyboardButton(text="Хочу окрыть внешний поиск", callback_data="wantOpenOut")
    button3 = types.InlineKeyboardButton(text="Подать заявку на поиск", callback_data="fetchOut")
    button5 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="recrut")
    button6 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button5)
    markup.row(button6)
    bot.send_message(message_chat_id, "Выбери вопрос по внешнему поиску:", reply_markup=markup)

def acceptOut(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="outSearch")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Пожалуйста, <b>направьте информацию по кандидату HR-партнеру</b> "
                                      "для согласования условий приема и запуска на согласование",
                     parse_mode = 'HTML', reply_markup=markup)


def wantOpenOut(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="outSearch")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Если у вас есть или в ближайшее время открывается позиция, "
                                      "вам необходимо <b>описать требования и обязанности</b> в рамках "
                                      "позиции в любом удобном формате и направить данную информацию HR-партнеру",
                     parse_mode='HTML', reply_markup=markup)


def fetchOut(message_chat_id, bot):
    button4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="outSearch")
    button5 = types.InlineKeyboardButton(text="🏠 Начало", callback_data="start")
    types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup()
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Когда-то тут будет бот по рекрутменту",
                     parse_mode = 'HTML', reply_markup=markup)

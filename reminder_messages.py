# Через один месяц
def func_time_delta1(message_chat_id, beginner_name, bot):
    bot.send_message(message_chat_id, "Добрый день!\nНовый сотрудник " + beginner_name + " работает в вашей команде "
                                                                                         "уже <b>месяц</b>!"
                                      "\nРекомендуем вам:\n"
                                      "1. Провести встречу по промежуточным результатам "
                                      "выполнения задания на испытательный срок\n"
                                      "2. Взять обратную связь у бадди и наставника по процессу "
                                      "вхождения нового сотрудника в компанию\n"
                                      "3. Взять обратную связь у нового сотрудника по его вхождению в компанию\n"
                                      "Если у вас будут оставаться вопросы, пожалуйста, обратитесь с HR-партнеру",
                     parse_mode='HTML')


def func_time_delta2(message_chat_id, beginner_name, bot):
    bot.send_message(message_chat_id, "Добрый день!\nНовый сотрудник " + beginner_name + " работает в вашей команде "
                                      "уже <b>два месяца</b>!\nПросим вас:\n"
                                      "1. Провести встречу по промежуточным результатам "
                                      "выполнения задания на испытательный срок \n"
                                      "2. Взять обратную связь у бадди и наставника по процессу вхождения нового "
                                      "сотрудника в компанию\n3. Взять обратную связь у нового сотрудника по его "
                                      "вхождению в компанию\nЕсли у вас будут оставаться вопросы, пожалуйста, "
                                                                                         "обратитесь с HR-партнеру",
                     parse_mode='HTML')


def func_time_delta3(message_chat_id, beginner_name, bot):
    bot.send_message(message_chat_id, "Добрый день!\nПодходит к концу испытательный срок сотрудника " + beginner_name +
                                      ".\n"
                                      "На этом этапе вам необходимо:\n1. Принять решение о продолжении взаимоотношений "
                                      "с сотрудником (справляется ли он с задачами, как прошел процесс вхождения в "
                                      "коллектив и компанию) \n"
                                      "2. Встретиться с новым сотрудником, подвести итоги испытательного срока и "
                                      "сообщить о своем решении"
                                      "\n<b>Важно</b>: если вы приняли решение расстаться с "
                                      "сотрудником, пожалуйста, обратитесь к HR-партнеру", parse_mode='HTML')

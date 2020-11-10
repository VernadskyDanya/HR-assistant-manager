# Почему-то не получается разделить код :(

def add_request(message_chat_id, leader_name, beginner_name, time_for_sql):
    # Класс для группировки данных в заявку
    class Request:
        def __init__(self, chat_id, leader_name, beginner_name, time):
            self.chat_id = chat_id
            self.leader_name = leader_name
            self.beginner_name = beginner_name
            self.time = time    # Время создания заявки

        def __repr__(self): # вызывается при операторе print
            return "<Request ('%s','%s', '%s', '%s')>" % (self.chat_id, self.leader_name, self.beginner_name, self.time)

    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///Requests_for_reminders.db', echo=True, connect_args={'check_same_thread': False})

    #   Создание таблицы в базе данных
    from sqlalchemy import Table, Column, Integer, String, MetaData, DATE
    metadata = MetaData()
    requests_table = Table('Requests', metadata,
                           Column('chat_id', Integer),
                           Column('leader_name', String),
                           Column('beginner_name', String, primary_key=True),
                           Column('time', DATE)
                           )
    metadata.create_all(engine)

    # Применим функцию mapper, чтобы создать отображение между Request и requests_table
    from sqlalchemy.orm import mapper
    mapper(Request, requests_table)

    # Создание сессии
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)  # Соединение с сессией
    session = Session()

    # Добавление новых объектов
    new_req = Request(message_chat_id, leader_name, beginner_name, time_for_sql)
    session.add(new_req)
    session.commit()

    for instance in session.query(Request):
        print(instance.chat_id, " ", instance.leader_name, " ", instance.time)


def send_reminder(bot):
    # Класс для группировки данных в заявку
    class Request:
        def __init__(self, chat_id, leader_name, beginner_name, time):
            self.chat_id = chat_id
            self.leader_name = leader_name
            self.beginner_name = beginner_name
            self.time = time  # Время создания заявки

        def __repr__(self):  # вызывается при операторе print
            return "<Request ('%s','%s', '%s', '%s')>" % (self.chat_id, self.leader_name, self.beginner_name, self.time)

    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///Requests_for_reminders.db', echo=False, connect_args={'check_same_thread': False})

    #   Создание таблицы в базе данных
    from sqlalchemy import Table, Column, Integer, String, MetaData, DATE
    metadata = MetaData()
    requests_table = Table('Requests', metadata,
                           Column('chat_id', Integer),
                           Column('leader_name', String),
                           Column('beginner_name', String, primary_key=True),
                           Column('time', DATE)
                           )
    metadata.create_all(engine)

    # Применим функцию mapper, чтобы создать отображение между Request и requests_table
    from sqlalchemy.orm import mapper
    mapper(Request, requests_table)

    # Создание сессии
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)  # Соединение с сессией
    session = Session()

    import time
    from datetime import date
    current_time = date(time.localtime()[0], time.localtime()[1], time.localtime()[2])  # Текущая дата
    from datetime import timedelta
    time_delta1 = timedelta(-30)
    time_delta2 = timedelta(-60)
    time_delta3 = timedelta(-74)
    for instance in session.query(Request):
        print(instance.time - current_time)
        if (instance.time - current_time) == time_delta1:
            from reminder_messages import func_time_delta1
            func_time_delta1(instance.chat_id, instance.beginner_name, bot)
        if (instance.time - current_time) == time_delta2:
            from reminder_messages import func_time_delta2
            func_time_delta2(instance.chat_id, instance.beginner_name, bot)
        if (instance.time - current_time) == time_delta3:
            from reminder_messages import func_time_delta3
            func_time_delta3(instance.chat_id, instance.beginner_name, bot)
    Session.close_all()


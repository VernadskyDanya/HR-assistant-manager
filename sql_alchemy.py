from sqlalchemy import create_engine
engine = create_engine('sqlite:///testSQLite.db', echo=True)

#   Создание таблицы в базе данных
from sqlalchemy import Table, Column, Integer, String, MetaData
metadata = MetaData()
requests_table = Table('Requests', metadata,
                       Column('chat_id', Integer),
                       Column('leader_name', String),
                       Column('beginner_name', String, primary_key=True),
                       Column('time', String)
                       )
metadata.create_all(engine)

# Применим функцию mapper, чтобы создать отображение между Request и requests_table
from sqlalchemy.orm import mapper
from request_struct import Request
mapper(Request, requests_table)

# Создание сессии
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)  # Соединение с сессией
session = Session()


# Добавление новых объектов
def add_reminder(new_request: Request):
    try:
        session.add(new_request)
        print("session.add(new_request)")
        session.commit()
        print("session.commit()")
        engine.connect().close()
    except:
        import logging
        logging.error("Problem in add_reminder function in sql_alchemy.py")


# Пробегаемся по бд
def scan_bd():
    for instance in session.query(Request):
        print(instance.chat_id, " ", instance.leader_name, " ", instance.time)


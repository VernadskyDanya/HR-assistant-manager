from sqlalchemy import create_engine
engine = create_engine('sqlite:///testSQLite.db', echo=True)


#   Создание таблицы в базе данных
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
requests_table = Table('Requests', metadata,
                       Column('chat.id', Integer),
                       Column('leader_name', String),
                       Column('beginner_name', String, primary_key=True),
                       Column('time', String)
                       )
metadata.create_all(engine)


# Класс для группировки данных в заявку
class Request:
    def __init__(self, chat_id, leader_name, beginner_name, time):
        self.chat_id = chat_id
        self.leader_name = leader_name
        self.beginner_name = beginner_name
        self.time = time    # Время создания заявки

    def __repr__(self): # вызывается при операторе print
        return "<Request ('%s','%s', '%s', '%s')>" % (self.chat_id, self.leader_name, self.beginner_name, self.time)


# Применим функцию mapper, чтобы создать отображение между Request и requests_table
from sqlalchemy.orm import mapper
mapper(Request, requests_table)

# Создание сессии
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)  # Соединение с сессией
session = Session()

# Добавление новых объектов
import time
#mmm = Request("56789", "Vasiliy Leader", "Ivan beginner", time.ctime())
#amm = Request("21421", "Maksim", "Ivan beginner", time.ctime())
#session.add(mmm)
#session.add(amm)
session.commit()

for instance in session.query(Request):
    print(instance.chat_id, "", instance.time)


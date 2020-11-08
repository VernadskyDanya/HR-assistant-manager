# Класс для группировки данных в заявку
class Request:
    def __init__(self, chat_id, leader_name, beginner_name, time):
        self.chat_id = chat_id
        self.leader_name = leader_name
        self.beginner_name = beginner_name
        self.time = time    # Время создания заявки

    def __repr__(self): # вызывается при операторе print
        return "<Request ('%s','%s', '%s', '%s')>" % (self.chat_id, self.leader_name, self.beginner_name, self.time)
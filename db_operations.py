# Метод добавления уведомления в бд
def add_request(message_chat_id, leader_name, beginner_name, time_for_db):

    # ПОДКЛЮЧАЕМСЯ К MONGOCLIENT
    import pymongo
    import passwords
    client = pymongo.MongoClient(passwords.mongodb_key)

    # ПОЛУЧАЕМ БАЗУ ДАННЫХ
    db = client['GN-reminders']

    # ПОЛУЧАЕМ КОЛЛЕКЦИЮ
    collection = db['Reminders-Adaptation']

    # ДОБАВЛЯЕМ В БД
    new_request = {"message_chat_id": message_chat_id,
               "beginner_name": beginner_name,
               "leader_name": leader_name,
               "time_for_db": time_for_db}

    db.posts.insert_one(new_request)


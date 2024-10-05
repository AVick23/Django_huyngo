import sqlite3

def read_questions_answers(database_path):
    pairs = []
    # Создание соединения с базой данных
    conn = sqlite3.connect(database_path)
    # Создание курсора
    c = conn.cursor()
    # Выполнение запроса SELECT для получения всех вопросов и ответов
    c.execute("SELECT questions, answers FROM Q_and_A")
    # Получение всех результатов запроса
    rows = c.fetchall()
    for row in rows:
        pairs.append({'question': row[0], 'answer': row[1]})
    # Закрытие соединения с базой данных
    conn.close()
    return pairs

# Загрузка вопрос-ответных пар из базы данных
question_answer_pairs = read_questions_answers('py_files/university.sqlite')


# # Ручное создание списка словарей вопрос-ответов
# question_answer_pairs = [
#     {'question': 'Как тебя зовут?', 'answer': 'Меня зовут бот.'},
#     {'question': 'Сколько тебе лет?', 'answer': 'Мне несколько месяцев.'},
#     {'question': 'Где ты живешь?', 'answer': 'Я живу в облаке данных.'},
#     # Добавьте сюда любые другие пары вопросов и ответов
# ]
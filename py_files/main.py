import sqlite3

def read_questions_answers(file_path):
    pairs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Разделение строки на вопрос и ответ без использования ':'
            question, answer = line.strip().split(' : ')
            pairs.append({'question': question, 'answer': answer})
    return pairs

# Загрузка вопрос-ответных пар из файла
question_answer_pairs = read_questions_answers('context2.txt')

# Создание соединения с базой данных
conn = sqlite3.connect('university.sqlite')

# Создание курсора
c = conn.cursor()

# Удаление всех существующих записей из таблицы
c.execute("DELETE FROM Q_and_A")

# Запись вопросов и ответов в базу данных
for pair in question_answer_pairs:
    c.execute("INSERT INTO Q_and_A (questions, answers) VALUES (?, ?)", (pair['question'], pair['answer']))

# Сохранение изменений
conn.commit()

# Закрытие соединения с базой данных
conn.close()

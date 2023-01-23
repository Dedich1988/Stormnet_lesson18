import sqlite3
import random

# создание и подключение к БД
connect = sqlite3.connect('my_database.db')

# создание курсора для выполение опараций над БД
cursor = connect.cursor()

# создание таблицы (если не существует)
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS car(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    model TEXT,
                    year INT,
                    color TEXT,
                    type TEXT)
    '''
)

# вставка нескольких строк в таблицу
cursor.execute(
    '''INSERT INTO car(model, year, color, type) 
       VALUES ('audi', 2010, 'white', 'diesel'),
              ('belgily', 2010, 'white', 'diesel'),
              ('mtz', 2010, 'white', 'diesel')
    '''
)

# вставка данных с использованием цикла и переменных
for i in range(20):
    model = random.choice(['audi', 'vw', 'tesla', 'mersedes'])
    year = random.randint(2000, 2022)
    color = random.choice(['yellow', 'white', 'black', 'red', 'blue'])
    type = random.choice(['diesel', 'gas', 'electric'])

    cursor.execute('''INSERT INTO car(model, year, color, type)
                     VALUES(?,?,?,?)''', (model, year, color, type))


# непосредственное выполнение изменений
connect.commit()
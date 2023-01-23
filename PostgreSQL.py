# работа с базой PostgreSQL
import psycopg2
from config import host, user, password, db_name

try:
    # подключение к существующей БД
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    # курсор для предоставления операций над БД
    # cursor = connection.cursor()

    # проверка версии БД
    with connection.cursor() as cursor:
        cursor.execute(
            'select version();'
        )
        print(f'Server version: {cursor.fetchone()}')

    # создание таблицы users
    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE users(
            id serial PRIMARY KEY,
            firs_name varchar(50) NOT NULL,
            nick_name varchar(50) NOT NULL);
            '''
        )
        print(f'Таблица успешно создана!')

    # вставка данных в таблицу
    with connection.cursor() as cursor:
        cursor.execute(
            '''INSERT INTO users(firs_name, nick_name)
            VALUES ('Igor', 'proger3000');
            '''
        )
        print(f'Данные успешно добавлены!')

    # выборка данных из таблицы
    with connection.cursor() as cursor:
        cursor.execute(
            '''SELECT nick_name FROM users WHERE firs_name = 'Igor';
            '''
        )
        print(cursor.fetchone())

    with connection.cursor() as cursor:
        cursor.execute(
            '''DROP TABLE users;
            '''
        )
        print('Таблица удалена!')

except Exception as e:
    print('Ошибка в процессе выполнения PostgresQL', e)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('[INFO] PostgreSQL соединение закрыто!')
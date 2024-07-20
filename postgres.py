import psycopg2

# Замените значения ниже на свои данные для подключения к PostgreSQL
DB_NAME = "pydb"
DB_USER = "pydb_user"
DB_PASSWORD = "pydb123"
DB_HOST = "localhost"  # например, "localhost" или "127.0.0.1"
DB_PORT = "5432"  # по умолчанию 5432

try:
    # Подключение к базе данных
    connection = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Создание курсора для выполнения SQL-запросов
    cursor = connection.cursor()

    # Пример SQL-запроса
    sql_query = "SELECT * FROM employees;"

    # Выполнение SQL-запроса
    cursor.execute(sql_query)

    # Получение результатов запроса
    results = cursor.fetchall()

    # Вывод результатов
    for row in results:
        print(row)

    # Закрытие курсора и подключения
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Ошибка при работе с PostgreSQL:", error)

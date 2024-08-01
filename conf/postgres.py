import psycopg2

DB_NAME = "pydb"
DB_USER = "pydb_user"
DB_PASSWORD = "pydb123"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    connection = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    cursor = connection.cursor()

    sql_query = "SELECT * FROM employees;"

    cursor.execute(sql_query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error in adapter PostgreSQL:", error)

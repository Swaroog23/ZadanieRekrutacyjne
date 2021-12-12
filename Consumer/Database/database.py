import sqlite3


def create_database_and_tables():
    with sqlite3.connect("key_value.db") as sql_conn:
        cursor = sql_conn.cursor()
        try:
            cursor.execute("""
                        CREATE TABLE key_values (
                            key INTEGER PRIMARY KEY,
                            value TEXT NOT NULL
                        )
                        """)
        except sqlite3.OperationalError:
            pass

def insert_data_to_db(key, value):
    with sqlite3.connect("key_value.db") as sql_conn:
        cursor = sql_conn.cursor()
        try:
            cursor.execute("INSERT INTO key_values VALUES (:key, :value)",
                            {'key': key, 'value': value})
            return 1
        except sqlite3.IntegrityError as error:
            return error


def get_data_from_db(key):
    with sqlite3.connect("key_value.db") as sql_conn:
        cursor = sql_conn.cursor()
        cursor.execute("SELECT value FROM key_values WHERE key=:key",
                        {'key': key})
        return cursor.fetchone()

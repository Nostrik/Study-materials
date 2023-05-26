import sqlite3

with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM table_2")
    result = cursor.fetchall()

    cursor.execute("SELECT count(*) FROM table_2")
    result2 = cursor.fetchall()

    cursor.execute("SELECT count(*) FROM table_3")
    result3 = cursor.fetchall()


if __name__ == "__main__":
    print(result, result2, result3)

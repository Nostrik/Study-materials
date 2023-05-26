import sqlite3

with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT count(DISTINCT id) FROM table_1")
    result = cursor.fetchall()

if __name__ == "__main__":
    print(result)


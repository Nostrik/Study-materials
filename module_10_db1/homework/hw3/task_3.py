import sqlite3
import pprint

with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM table_2")
    result = cursor.fetchall()

if __name__ == "__main__":
    pprint.pprint(result)

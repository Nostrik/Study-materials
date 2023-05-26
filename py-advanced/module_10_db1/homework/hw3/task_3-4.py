import sqlite3

with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT count(*)FROM(SELECT value FROM table_1 INTERSECT SELECT value FROM table_2 "
                   "INTERSECT SELECT value FROM table_3)")
    result = cursor.fetchall()

if __name__ == "__main__":
    print(result)

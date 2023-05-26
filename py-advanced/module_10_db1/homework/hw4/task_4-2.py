import sqlite3

with sqlite3.connect("hw_4_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT round((SELECT avg(salary) FROM salaries), 2)")
    result = cursor.fetchall()

if __name__ == "__main__":
    print(result)

import sqlite3

with sqlite3.connect("hw_4_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT salary FROM (SELECT salary FROM salaries ORDER BY salary ASC LIMIT 36635)"
                   " ORDER by salary DESC LIMIT 2")
    result = cursor.fetchall()

if __name__ == "__main__":
    print((result[0][0] + result[1][0]) / 2)

import sqlite3

delete_request = """
DELETE FROM `table_stars`
    WHERE name LIKE 'А%';
"""

if __name__ == "__main__":
    with sqlite3.connect("db_stars.db") as conn:
        cursor = conn.cursor()

        cursor.execute(delete_request)

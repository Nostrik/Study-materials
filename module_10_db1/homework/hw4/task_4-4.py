import sqlite3

all_notes_in_salaries = "SELECT count(*) FROM salaries"

sum_salary_10per_people = "CAST((SELECT sum(salary) FROM (SELECT salary FROM salaries ORDER by salary DESC LIMIT" \
                          " (SELECT count(*) FROM salaries) * 0.1)) as real)"

sum_salary_90per_people = "CAST((SELECT sum(salary) FROM (SELECT salary FROM salaries ORDER by salary ASC LIMIT " \
                          "(SELECT count(*) FROM salaries) * 0.9)) as real)"


with sqlite3.connect("hw_4_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT 100 * round(CAST((SELECT sum(salary) FROM (SELECT salary FROM salaries ORDER by salary "
                   "DESC LIMIT (SELECT count(*) FROM salaries) * 0.1)) as real)/CAST((SELECT sum(salary) "
                   "FROM (SELECT salary FROM salaries ORDER by salary ASC LIMIT (SELECT count(*) FROM salaries) * 0.9))"
                   " as real), 2)")
    result = cursor.fetchall()

if __name__ == "__main__":
    print(result)

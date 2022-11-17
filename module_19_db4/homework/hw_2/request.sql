SELECT avg(grade) as avg_grade,
students.full_name
FROM assignments_grades
LEFT OUTER JOIN students
on assignments_grades.student_id = students.student_id
GROUP by assignments_grades.student_id
ORDER by avg_grade DESC
LIMIT 10
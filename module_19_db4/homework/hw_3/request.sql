SELECT avg(grade) as avg_grade,
students.full_name
FROM assignments_grades
JOIN assignments
ON assignments_grades.assisgnment_id = assignments.assisgnment_id
JOIN students
ON assignments_grades.student_id = students.student_id
GROUP by assignments.teacher_id
order by avg_grade desc

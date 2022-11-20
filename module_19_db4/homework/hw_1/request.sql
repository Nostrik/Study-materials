SELECT avg(grade),
teachers.full_name
FROM assignments_grades
JOIN assignments
ON assignments_grades.assisgnment_id = assignments.assisgnment_id
JOIN teachers
ON assignments.teacher_id = teachers.teacher_id
GROUP BY assignments.teacher_id
LIMIT 1
SELECT avg(assignments_grades.grade),
max(assignments_grades.grade),
min(assignments_grades.grade)
FROM assignments_grades
JOIN assignments
ON assignments_grades.assisgnment_id = assignments.assisgnment_id
WHERE assignments_grades.date > assignments.due_date AND assignments.assisgnment_id = 1


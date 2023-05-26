SELECT
avg(assignments_grades.grade)
FROM assignments
JOIN assignments_grades
ON assignments.assisgnment_id = assignments_grades.assisgnment_id
WHERE assignments.assignment_text like 'выучить%'
OR assignments.assignment_text like 'прочитать%'
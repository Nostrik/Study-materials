SELECT avg(grade), teacher_id
FROM assignments_grades
INNER JOIN assignments
ON assignments_grades.assisgnment_id = assignments.assisgnment_id
GROUP by assignments.teacher_id
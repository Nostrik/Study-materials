SELECT count(*)
FROM students

SELECT avg(assignments_grades.grade),
assignments_grades.student_id
FROM students
JOIN assignments_grades
ON students.student_id = assignments_grades.student_id
GROUP by assignments_grades.student_id

SELECT count(*)
FROM
(SELECT *
FROM students
JOIN assignments_grades
ON students.student_id = assignments_grades.student_id
WHERE assignments_grades.grade = 0
GROUP by assignments_grades.student_id)

SELECT count(*)
FROM
(SELECT *
FROM students
JOIN assignments_grades
ON students.student_id = assignments_grades.student_id
JOIN assignments
ON assignments_grades.assisgnment_id = assignments.assisgnment_id
WHERE assignments.due_date < assignments_grades.date
GROUP by assignments_grades.student_id)

SELECT count(*)
FROM assignments_grades
WHERE grade = 0
ORDER by student_id
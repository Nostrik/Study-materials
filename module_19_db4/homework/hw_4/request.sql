SELECT avg(assignments_grades.grade),
max(assignments_grades.grade),
min(assignments_grades.grade)
FROM assignments_grades
JOIN assignments
ON assignments_grades.assisgnment_id = assignments.assisgnment_id
WHERE assignments_grades.date > assignments.due_date AND assignments.assisgnment_id = 1

SELECT *
FROM
(SELECT assignments.group_id,
assignments.due_date,
asg.date
FROM assignments
INNER JOIN assignments_grades asg
ON assignments.assisgnment_id = asg.assisgnment_id
WHERE asg.date > assignments.due_date)
ORDER by group_id

SELECT count(*)
FROM
(SELECT assignments.due_date as DUE_DATE,
assignments_grades.date as DATE,
assignments.group_id as GROUP_ID
FROM assignments
INNER JOIN assignments_grades
ON assignments.assisgnment_id = assignments_grades.assisgnment_id)
WHERE DATE > DUE_DATE


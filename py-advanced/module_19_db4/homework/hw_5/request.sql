-- обще количество учеников
SELECT count(*)
FROM students

-- количество учеников
SELECT sg.group_id,
       count(*) AS students_count
FROM students
INNER JOIN students_groups sg on sg.group_id = students.group_id
GROUP BY sg.group_id;

-- средняя оценка
SELECT sg.group_id,
       avg(ag.grade) AS students_count
FROM students
INNER JOIN students_groups sg on sg.group_id = students.group_id
INNER JOIN assignments_grades ag on students.student_id = ag.student_id
GROUP BY sg.group_id
ORDER BY students_count;

-- количество учеников, которые не сдали работы
SELECT sg.group_id,
       count(ag.student_id)
FROM students
INNER JOIN students_groups sg on sg.group_id = students.group_id
INNER JOIN
    (SELECT DISTINCT student_id
    FROM
        (SELECT sum(grade) AS sum_grade,
            student_id
        FROM assignments_grades
        GROUP BY assisgnment_id, student_id
        HAVING sum_grade > 0)) ag on students.student_id = ag.student_id
GROUP BY sg.group_id;

-- количество учеников, которые просрочили дедлайн
SELECT sg.group_id,
       count(ag.student_id)
FROM students
INNER JOIN students_groups sg on sg.group_id = students.group_id
INNER JOIN
    (SELECT DISTINCT student_id
    FROM
        (SELECT student_id
        FROM assignments_grades
        INNER JOIN assignments a on assignments_grades.assisgnment_id = a.assisgnment_id
        WHERE a.due_date < assignments_grades.date)) ag on students.student_id = ag.student_id
GROUP BY sg.group_id;

-- количество повторных попыток сдать работу
SELECT sg.group_id,
       count(ag.student_id) as students_count,
       sum(ag.count - 1) as additional_attempts_count
FROM students
INNER JOIN students_groups sg on sg.group_id = students.group_id
INNER JOIN
    (SELECT student_id, assisgnment_id, sum(grade), count(*) AS count
    FROM assignments_grades
    GROUP BY student_id, assisgnment_id
    HAVING count > 1) ag on students.student_id = ag.student_id
GROUP BY sg.group_id;
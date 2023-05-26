SELECT assignments_grades.student_id,
       full_name
FROM students
INNER JOIN assignments_grades ON students.student_id = assignments_grades.student_id AND
    assignments_grades.assisgnment_id in
        (SELECT assisgnment_id
        FROM assignments
        INNER JOIN
            (SELECT avg(ag.grade) AS avg_grade,
               teachers.teacher_id AS t_id
            FROM teachers
            INNER JOIN assignments a ON teachers.teacher_id = a.teacher_id
            INNER JOIN assignments_grades ag ON a.assisgnment_id = ag.assisgnment_id
            GROUP BY t_id
            ORDER BY avg_grade Desc
            LIMIT 1) min_t ON teacher_id = min_t.t_id)

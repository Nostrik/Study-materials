SELECT A.group_id,
        avg(AG.grade) as Average,
        max(AG.grade) as Maximum,
        min(AG.grade) as Minimum
FROM assignments_grades AG
    JOIN assignments A
    ON AG.assisgnment_id = A.assisgnment_id
WHERE AG.date > A.due_date
GROUP BY A.group_id


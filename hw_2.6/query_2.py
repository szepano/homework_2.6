import sqlite3

sql = '''WITH subject_top_students AS (
    SELECT
        grades.subj AS subject,
        grades.stud_id,
        AVG(grades.grade) AS average_grade
    FROM
        grades
    GROUP BY
        grades.subj,
        grades.stud_id
    HAVING
        AVG(grades.grade) = (
            SELECT
                MAX(avg_grades.average_grade)
            FROM (
                SELECT
                    AVG(grades.grade) AS average_grade
                FROM
                    grades
                WHERE
                    grades.subj = subject
                GROUP BY
                    grades.stud_id
            ) avg_grades
        )
)
SELECT
    subject_top_students.subject,
    students.id AS student_id,
    students.name AS student_name,
    subject_top_students.average_grade
FROM
    subject_top_students
JOIN
    students ON subject_top_students.stud_id = students.id;
'''




def execute(sql: str):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute(sql))
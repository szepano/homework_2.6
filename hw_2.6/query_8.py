import sqlite3

sql = '''SELECT
            grades.subj AS subject,
            teachers.teacher AS teacher,
            AVG(grades.grade) AS average_grade
        FROM
            grades
        JOIN
            subjects ON grades.subj = subjects.subject
        JOIN
            teachers ON subjects.teaches = teachers.teacher
        GROUP BY
            grades.subj, teachers.teacher;
            '''

def execute(sql: str):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute(sql))
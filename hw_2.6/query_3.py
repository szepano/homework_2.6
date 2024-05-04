import sqlite3

sql = '''SELECT
            groups.group_id AS group_id,
            grades.subj AS subject,
            AVG(grades.grade) AS average_grade
        FROM grades
        JOIN
            students ON grades.stud_id = students.id
        JOIN
            groups ON students.id = groups.student
        JOIN
            subjects ON grades.subj = subjects.subject
        GROUP BY
            groups.group_id, grades.subj
        ORDER BY
            groups.group_id, grades.subj;
        '''

def execute(sql: str):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute(sql))
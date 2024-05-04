import sqlite3

sql = '''SELECT
            students.name AS student,
            teachers.teacher AS teacher_name,
            subjects.subject AS course
        FROM grades
        JOIN
            students ON grades.stud_id = students.id
        JOIN
            subjects ON grades.subj = subjects.subject
        JOIN
            teachers ON subjects.teaches = teachers.teacher
        WHERE
            students.id = 15
            AND teachers.id = 2;
            '''

def execute(sql: str):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute(sql))
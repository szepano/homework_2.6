import sqlite3

sql = '''SELECT
    subjects.subject,
    teachers.teacher AS teacher_name
FROM
    subjects
JOIN
    teachers ON subjects.teaches = teachers.teacher;
'''


def execute(sql: str):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute(sql))
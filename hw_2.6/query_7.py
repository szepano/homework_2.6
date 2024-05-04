import sqlite3

sql = '''SELECT
            grades.subj AS subject,
            groups.group_id AS group_id,
            GROUP_CONCAT(grades.grade, ', ') AS grades
        FROM grades
        JOIN
            groups ON grades.stud_id = groups.student
        JOIN
            students ON groups.student = students.id
        GROUP BY grades.subj, groups.group_id
        ORDER BY grades.subj, groups.group_id;'''

def execute(sql: str):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute(sql))
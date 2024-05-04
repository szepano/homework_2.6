import sqlite3

sql = '''SELECT
            groups.group_id AS group_id,
            AVG(grades.grade) AS average_grade
        FROM groups
        JOIN
            grades ON grades.stud_id = groups.student
        GROUP BY
            groups.group_id
        '''

def execute(sql: str):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute(sql))
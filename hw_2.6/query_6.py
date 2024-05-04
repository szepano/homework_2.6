import sqlite3

sql = '''SELECT
            groups.group_id as group_id,
            GROUP_CONCAT(students.name, ', ') AS student
        FROM groups
        JOIN
            students ON groups.student = students.id
        GROUP BY
            groups.group_id
        ORDER BY
            groups.group_id;'''

def execute(sql: str):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute(sql))
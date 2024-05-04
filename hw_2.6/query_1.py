import sqlite3

sql = '''SELECT
            students.id AS student_id,
            students.name AS student_name,
            AVG(grades.grade) AS average_grade
        FROM 
            students
        JOIN
            grades ON students.id = grades.stud_id
        GROUP BY
            students.id, students.name
        ORDER BY
            average_grade DESC
        LIMIT
            5'''

def execute(sql: str):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute(sql))
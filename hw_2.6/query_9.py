import sqlite3

sql = '''SELECT
            students.name AS student,
            GROUP_CONCAT(unique_subjects.subj, ', ') AS subjects
        FROM students
        JOIN
            (SELECT stud_id, subj
            FROM grades
            GROUP BY stud_id, subj) AS unique_subjects
        ON
            students.id = unique_subjects.stud_id 
        GROUP BY
            students.id, students.name;'''




def execute(sql: str):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute(sql))
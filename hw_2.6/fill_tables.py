from datetime import datetime
import faker
from random import randint, choice, sample, shuffle
import sqlite3

GROUPS = 3
STUDENTS = randint(30, 50)
TEACHERS = randint(3, 5)
SUBJECTS = randint(5, 8)
INDEXES_STUDENTS = list(range(1, STUDENTS))
def generate_fake_data(students, teachers, subjects) -> tuple():
    
    fake_studs = []
    fake_teachers = []
    fake_subj =[]

    fake = faker.Faker('pl_PL')

    for _ in range(students):
        fake_studs.append(fake.name())

    for _ in range(teachers):
        fake_teachers.append(fake.name())

    for _ in range(subjects):
        fake_subj.append(fake.job())
    
    return fake_studs, fake_teachers, fake_subj

def prepare_data(students, teachers, subjects, groups=INDEXES_STUDENTS) -> tuple():
    
    for_groups = []
    shuffle(groups)
    n = len(groups)
    for_groups.append(tuple(groups[:n//3], ))
    for_groups.append(tuple(groups[n//3:2*n//3], ))
    for_groups.append(tuple(groups[2*n//3:], ))
    


    for_studs = []
    for student in students:
        for_studs.append((student, ))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher, ))
    
    for_subjects = []
    for sub in subjects:
        for_subjects.append((sub, choice(teachers)))

    return for_studs, for_teachers, for_subjects, for_groups


def insert_data(students, teachers, subjects, groups):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        
        sql_to_students = '''INSERT INTO students(name)
                            VALUES (?)'''
        cur.executemany(sql_to_students, students)

        sql_to_teachers = '''INSERT INTO teachers(teacher)
                            VALUES (?)'''
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = '''INSERT INTO subjects(subject, teaches)
                            VALUES (?, ?)'''
        cur.executemany(sql_to_subjects, subjects)

        sql_to_groups = '''INSERT INTO groups(students)
                           VALUES(?)'''
        new_groups = [(str(student_id),) for group in groups for student_id in group]
        cur.executemany(sql_to_groups, new_groups)

if __name__ == '__main__':
    students, teachers, subjects, groups = prepare_data(*generate_fake_data(STUDENTS, TEACHERS, SUBJECTS))
    print(students)
    print(groups)
    insert_data(students, teachers, subjects, groups)
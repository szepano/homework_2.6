import faker
from random import randint, choice, shuffle
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


def prepare_data(students, teachers, subjects, stud_id=INDEXES_STUDENTS, groups=GROUPS) -> tuple():
    
    for_groups = []
    shuffle(stud_id)
    for i in stud_id:
        for_groups.append((randint(1, groups), i, ))
    
    
    for_grades = []
    for id in stud_id:
        for i in range(1, randint(10, 20)):
            for_grades.append((id, randint(1, 6), choice(subjects), ))

    for_studs = []
    for student in students:
        for_studs.append((student, ))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher, ))
    
    for_subjects = []
    for sub in subjects:
        for_subjects.append((sub, choice(teachers)))

    return for_studs, for_teachers, for_groups, for_subjects, for_grades


def insert_data(students, teachers, groups, subjects, grades):
    with sqlite3.connect('tables1.db') as con:
        cur = con.cursor()
        
        sql_to_students = '''INSERT INTO students(name)
                            VALUES (?)'''
        cur.executemany(sql_to_students, students)

        sql_to_teachers = '''INSERT INTO teachers(teacher)
                            VALUES (?)'''
        cur.executemany(sql_to_teachers, teachers)
        
        sql_to_groups = '''INSERT INTO groups(group_id, student)
                           VALUES(?, ?)'''
        cur.executemany(sql_to_groups, groups)

        sql_to_subjects = '''INSERT INTO subjects(subject, teaches)
                            VALUES (?, ?)'''
        cur.executemany(sql_to_subjects, subjects)

        sql_to_grades = '''INSERT INTO grades(stud_id, grade, subj)
                            VALUES (?, ?, ?)'''
        cur.executemany(sql_to_grades, grades)

if __name__ == '__main__':
    students, teachers, groups, subjects, grades = prepare_data(*generate_fake_data(STUDENTS, TEACHERS, SUBJECTS))
    insert_data(students, teachers, groups, subjects, grades)
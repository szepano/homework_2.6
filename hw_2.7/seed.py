import faker
from base import Student, Group, Teacher, Subject, Grade, session
from random import randint, choice



STUDENTS = randint(30, 50)
GROUPS = 3
TEACHERS = randint(3, 5)
SUBJECTS = randint(5, 8)
INDEXES = list(range(1, STUDENTS))

def generate_fake_data(students, teachers, subjects):
    
    fake_studs = []
    fake_teachers = []
    fake_subjects = []
    fake = faker.Faker('pl_PL')
    
    for _ in range(students):
        fake_studs.append(fake.name())

    for _ in range(teachers):
        fake_teachers.append(fake.name())

    for _ in range(subjects):
        fake_subjects.append(fake.job())

    return fake_studs, fake_teachers, fake_subjects

def prepare_data(students, teachers, subjects, stud_id=INDEXES, groups=GROUPS):
    
    for_students = students
    for_teachers = teachers
    for_groups = []
    for i in stud_id:
        for_groups.append([randint(1, groups), i])

    for_grades = []
    for id in stud_id:
        for i in range(1, randint(1, 20)):
            for_grades.append([id, randint(1, 6), choice(subjects)])

    for_subjects = []
    for sub in subjects:
        for_subjects.append([sub, randint(1, len(teachers))])

    return for_students, for_groups, for_teachers, for_subjects, for_grades

def insert_data(students, groups, teachers, subjects, grades):

    print(students[0])
    try:
        for stud in students:
            session.add(Student(name=stud))
        print('students inserted')
        session.commit()
    except Exception as e:
        session.rollback()
        print('dane cofnięte')
        print(e)
        return

    print(groups[0])
    try:
        for group in groups:
            session.add(Group(id=group[0], stud_id=group[1]))
        print('groups inserted')
        session.commit()
    except Exception as e:
        session.rollback()
        print('dane cofnięte')
        print(e)
        return
    
    print(teachers[0])
    try:
        for teacher in teachers:
            session.add(Teacher(name=teacher))
        print('teachers inserted')
        session.commit()
    except Exception as e:
        session.rollback()
        print('dane cofnięte')
        print(e)
        return

    print(subjects[0])
    try:
        for subject in subjects:
            session.add(Subject(subject=subject[0], teaches=subject[1]))
        print('subjects inserted')
        session.commit()
    except Exception as e:
        session.rollback()
        print('dane cofnięte')
        print(e)
        return

    print(grades[0])
    try:
        for gr in grades:
            session.add(Grade(stud_id=gr[0], grade=gr[1], subject=gr[2]))
        print('grades inserted')
        session.commit()
    except Exception as e:
        session.rollback()
        print('dane cofnięte')
        print(e)
        return
    


if __name__ == '__main__':
    students, groups, teachers, subjects, grades = prepare_data(*generate_fake_data(STUDENTS, TEACHERS, SUBJECTS))
    insert_data(students, groups, teachers, subjects, grades)
    

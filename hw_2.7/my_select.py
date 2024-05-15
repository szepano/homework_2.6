from base import Student, Group, Teacher, Subject, Grade, session, func
from sqlalchemy import select

def select_1():

    query = (
        select(Student.name, func.avg(Grade.grade).label('average_grade'))
        .order_by(func.avg(Grade.grade).desc())
        .group_by(Student.name)
        .join(Student)
        .limit(5)
    )
    for i in session.execute(query):
        print(i)

def select_2():
    
    query = (
        select(
            Subject.subject,
            Student.name,
            func.avg(Grade.grade).label('average_grade')
        )
        .join(Grade, Subject.subject == Grade.subject)
        .join(Student, Grade.stud_id == Student.id)
        .order_by(Subject.subject, func.avg(Grade.grade).desc())
        .distinct(Subject.subject)
        .group_by(Subject.subject, Student.name)
    )
    
    for i in session.execute(query):
        print(i)

def select_3():

    query = (
        select(Group.id, Subject.subject, func.avg(Grade.grade))
        .join(Student, Grade.stud_id == Student.id)
        .join(Subject, Grade.subject == Subject.subject)
        .group_by(Group.id, Subject.subject)
        .order_by(Subject.subject)
    )

    for i in session.execute(query):
        print(i)

def select_4():

    query = (
        select(Group.id, func.avg(Grade.grade))
        .join(Student, Group.stud_id == Student.id)
        .join(Grade, Student.id == Grade.stud_id)
        .group_by(Group.id)
    )

    for i in session.execute(query):
        print(i)

def select_5():

    teach_id = 3

    query = (
        select(Teacher.name, Subject.subject)
        .join(Subject, Subject.teaches == Teacher.id)
        .where(Teacher.id == teach_id)
        .group_by(Teacher.name, Subject.subject)
    )

    for i in session.execute(query):
        print(i)

def select_6():

    group = 3

    query = (
        select(Group.id, Student.name)
        .join(Student, Student.id == Group.stud_id)
        .where(Group.id == group)
        .group_by(Group.id, Student.name)
    )

    for i in session.execute(query):
        print(i)

def select_7():

    group = 2
    subject = 'Kupiec'
    # subject jest jako nazwa zamiast id, ponieważ w mojej bazie danych wystąpił błąd i subjects.id się nie wypełniło

    query = (
        select(Student.name, Subject.subject, Grade.grade)
        .select_from(Group)
        .join(Student, Group.stud_id == Student.id)
        .join(Grade, Student.id == Grade.stud_id)
        .join(Subject, Grade.subject == Subject.subject)
        .where(Group.id == group)
        .where(Subject.id == subject)
    )

    for i in session.execute(query):
        print(i)

def select_8():

    teacher = 3

    query =(
        select(Teacher.name, func.avg(Grade.grade))
        .join(Subject, Subject.teaches == Teacher.id)
        .join(Grade, Grade.subject == Subject.subject)
        .where(Teacher.id == teacher)
        .group_by(Teacher.name)
    )

    for i in session.execute(query):
        print(i)

def select_9():
    id_student = 4

    query = (
        select(Student.name, Student.id, Subject.subject)
        .join(Grade, Grade.stud_id == Student.id)
        .where(Student.id == id_student)
        .group_by(Student.name, Student.id, Subject.subject)
    )

    for i in session.execute(query):
        print(i)

def select_10():
    teach_id = 3
    id_student = 23

    query = (
        select(Student.name, Subject.subject, Teacher.name)
        .join(Grade, Grade.stud_id == Student.id)  # Join Grade with Student
        .join(Subject, Grade.subject == Subject.subject)  # Join Grade with Subject
        .join(Teacher, Teacher.id == Subject.teaches)  # Join Teacher with Subject
        .where(Student.id == id_student)
        .where(Teacher.id == teach_id)
    )

    for i in session.execute(query):
        print(i)

if __name__ == '__main__':
    # select_1()
    # select_2()
    # select_3()
    # select_4()
    # select_5()
    # select_6()
    # select_7()
    # select_8()
    # select_9()
    # select_10()
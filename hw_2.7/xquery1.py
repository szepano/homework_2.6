from base import Student, Grade, session, func
from sqlalchemy import select



if __name__ == '__main__':
    subquery = (
        select(Student.name, func.avg(Grade.grade).label('average_grade'))
        .order_by(func.avg(Grade.grade).desc())
        .group_by(Student.name)
        .join(Student)
        .limit(5)
    )
    
    count = 0
    for u in session.execute(subquery):
        print(u)
        count += 1
    print(count)
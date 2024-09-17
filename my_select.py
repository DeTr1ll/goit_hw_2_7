from sqlalchemy import func, select
from models import Student, Course, Grade, Group, Teacher
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:pass@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()

# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    return session.query(Student).join(Grade).group_by(Student.id).order_by(func.avg(Grade.score).desc()).limit(5).all()

# 2. Знайти студента із найвищим середнім балом з певного предмета
def select_2(course_id):
    return session.query(Student).join(Grade).filter(Grade.course_id == course_id).group_by(Student.id).order_by(func.avg(Grade.score).desc()).first()

# 3. Знайти середній бал у групах з певного предмета
def select_3(group_id, course_id):
    return session.query(func.avg(Grade.score)).join(Student).filter(Student.group_id == group_id, Grade.course_id == course_id).scalar()

# 4. Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4():
    return session.query(func.avg(Grade.score)).scalar()

# 5. Знайти які курси читає певний викладач
def select_5(teacher_id):
    return session.query(Course).filter(Course.teacher_id == teacher_id).all()

# 6. Знайти список студентів у певній групі
def select_6(group_id):
    return session.query(Student).filter(Student.group_id == group_id).all()

# 7. Знайти оцінки студентів у окремій групі з певного предмета
def select_7(group_id, course_id):
    return session.query(Grade).join(Student).filter(Student.group_id == group_id, Grade.course_id == course_id).all()

# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(teacher_id):
    return session.query(func.avg(Grade.score)).join(Course).filter(Course.teacher_id == teacher_id).scalar()

# 9. Знайти список курсів, які відвідує певний студент
def select_9(student_id):
    return session.query(Course).join(Grade).filter(Grade.student_id == student_id).distinct().all()

# 10. Список курсів, які певному студенту читає певний викладач
def select_10(student_id, teacher_id):
    return session.query(Course).join(Grade).filter(Grade.student_id == student_id, Course.teacher_id == teacher_id).all()
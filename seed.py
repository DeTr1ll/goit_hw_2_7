from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Base, Student, Group, Teacher, Course, Grade
import random

engine = create_engine('postgresql://postgres:pass@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

groups = [Group(name=fake.word()) for _ in range(3)]
teachers = [Teacher(name=fake.name()) for _ in range(5)]
courses = [Course(name=fake.word(), teacher=random.choice(teachers)) for _ in range(8)]
students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(30)]

for student in students:
    for _ in range(20):
        grade = Grade(
            student=student,
            course=random.choice(courses),
            score=random.uniform(1, 10)
        )
        session.add(grade)

session.add_all(groups + teachers + courses + students)
session.commit()
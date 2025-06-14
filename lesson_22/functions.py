from models import get_session, Student, Course
from faker import Faker
import random


session = get_session()
faker = Faker()


def create_courses():
    course_names = ["Math", "Physics", "Biology", "History", "Programming"]
    for name in course_names:
        if not session.query(Course).filter_by(name=name).first():
            session.add(Course(name=name))
    session.commit()

def create_random_students(n=20):
    courses = session.query(Course).all()
    for _ in range(n):
        student = Student(
            name=faker.name(),
            email=faker.unique.email()
        )
        student.courses = random.sample(courses, k=random.randint(1, 3))
        session.add(student)
    session.commit()

def add_student(name, email, course_ids):
    student = Student(name=name, email=email)
    student.courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
    session.add(student)
    session.commit()

def get_students_by_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    return course.students if course else []

def get_courses_by_student(email):
    student = session.query(Student).filter_by(email=email).first()
    return student.courses if student else []

def update_student_email(old_email, new_email):
    student = session.query(Student).filter_by(email=old_email).first()
    if student:
        student.email = new_email
        session.commit()

def delete_student(email):
    student = session.query(Student).filter_by(email=email).first()
    if student:
        session.delete(student)
        session.commit()


if __name__ == '__main__':
    create_courses()
    create_random_students(20)

    print("=== Students in Programming ===")
    for s in get_students_by_course("Programming"):
        print(f"{s.name} - {s.email}")

    print("=== Courses for first student ===")
    first_student = session.query(Student).first()
    print(f"{first_student.name}: {[c.name for c in get_courses_by_student(first_student.email)]}")

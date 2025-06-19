from db_client import DBClient
from models import Base


def main():
    db = DBClient()

    Base.metadata.create_all(db.engine)

    course = db.add_course("Manual QA Fundamentals")
    print("Курс:", course)

    student = db.add_student("Олександр QA", 35, course_ids=[course.id])
    print("Студент:", student)

    print("\nСтуденты на курсе:", db.get_students_by_course(course.id))
    print("Курсы студента:", db.get_courses_by_student(student.id))

    db.update_student_age(student.id, 36)
    print("\nПосле обновления возраста:", db.get_students_by_course(course.id)[0])

    db.delete_student(student.id)
    print("\nПосле удаления студента:", db.get_students_by_course(course.id))


if __name__ == "__main__":
    main()

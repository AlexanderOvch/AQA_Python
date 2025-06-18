from typing import List, Optional
from sqlalchemy import create_engine, update, delete
from sqlalchemy.orm import sessionmaker, joinedload
from models import Base, Student, Course, student_course
import config


class DBClient:

    def __init__(self, echo: bool = False):
        self.engine = create_engine(
            f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}"
            f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
            echo=echo,
            future=True
        )
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine, autoflush=False)

    def add_course(self, title: str) -> Course:
        """Создаёт курс, если такого ещё нет, иначе возвращает существующий."""
        with self.Session() as s:
            existing = s.query(Course).filter_by(title=title).first()
            if existing:
                return existing
            course = Course(title=title)
            s.add(course)
            s.commit()
            s.refresh(course)
            return course

    def add_student(
        self,
        name: str,
        age: int,
        course_ids: Optional[List[int]] = None
    ) -> Student:
        with self.Session() as s:
            student = Student(name=name, age=age)
            if course_ids:
                courses = s.query(Course).filter(Course.id.in_(course_ids)).all()
                student.courses.extend(courses)
            s.add(student)
            s.commit()
            s.refresh(student)
            return student

    def get_students_by_course(self, course_id: int) -> List[Student]:
        with self.Session() as s:
            course = (
                s.query(Course)
                .options(joinedload(Course.students))
                .filter(Course.id == course_id)
                .first()
            )
            return course.students if course else []

    def get_courses_by_student(self, student_id: int) -> List[Course]:
        with self.Session() as s:
            student = (
                s.query(Student)
                .options(joinedload(Student.courses))
                .filter(Student.id == student_id)
                .first()
            )
            return student.courses if student else []

    def update_student_age(self, student_id: int, new_age: int) -> None:
        with self.Session() as s:
            s.execute(
                update(Student)
                .where(Student.id == student_id)
                .values(age=new_age)
            )
            s.commit()

    # ---------- DELETE ----------
    def delete_student(self, student_id: int) -> None:
        with self.Session() as s:
            student = s.get(Student, student_id)
            if student:
                student.courses.clear()   # убираем связи в student_course
                s.delete(student)
                s.commit()

    def delete_course(self, course_id: int) -> None:
        with self.Session() as s:
            course = s.get(Course, course_id)
            if course:
                course.students.clear()
                s.delete(course)
                s.commit()

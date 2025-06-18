from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

student_course = Table(
    "student_course", Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id", ondelete="CASCADE")),
    Column("course_id",  Integer, ForeignKey("courses.id",  ondelete="CASCADE"))
)

class Student(Base):
    __tablename__ = "students"

    id   = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age  = Column(Integer, nullable=False)

    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students",
    )

    def __repr__(self):
        return f"<Student {self.id} {self.name} ({self.age})>"

class Course(Base):
    __tablename__ = "courses"

    id    = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)

    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses",
    )

    def __repr__(self):
        return f"<Course {self.id} {self.title}>"

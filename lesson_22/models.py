from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()


student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)

    courses = relationship('Course', secondary=student_course, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    students = relationship('Student', secondary=student_course, back_populates='courses')



def get_session():
    engine = create_engine('postgresql://postgres:password@localhost:5432/studentdb')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

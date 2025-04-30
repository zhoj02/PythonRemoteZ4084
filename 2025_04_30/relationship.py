from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


# connection string
db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/relationships')

# create salary and employye class with Base, import declarative_base
# use relantionship in the class from sql alchemy

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    salary = relationship("Salary", back_populates="employees")


class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    date_from = Column(Date)
    employees = relationship("Employee", back_populates="salary")

# create the tables
Base.metadata.create_all(db)
# create a session
Session = sessionmaker(bind=db)
session = Session()
# create a new employee
employee = Employee(name='John Doe')
# create a new salary
salary = Salary(amount=50000, employee_id=1, date_from='2025-04-30')

# add the employee and salary to the session
session.add(employee)
session.add(salary)
session.commit()

# query the employee
print(session.query(Employee).filter_by(name='John Doe').first().salary)
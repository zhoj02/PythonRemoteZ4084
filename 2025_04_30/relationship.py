from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


# connection string
db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/relationships')

# create salary and employye class with Base, import declarative_base
# use relantionship in the class from sql alchemy

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # salary_id = Column(Integer, ForeignKey('salary.id'))

    salary = relationship("Salary", back_populates="employees")


class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employees = relationship("Employee", back_populates="salary")

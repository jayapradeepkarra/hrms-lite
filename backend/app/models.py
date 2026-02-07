from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(50), unique=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    department = Column(String(100), nullable=False)

# class Attendance(Base):
#     __tablename__ = "attendance"

#     id = Column(Integer, primary_key=True)
#     employee_id = Column(Integer, ForeignKey("employees.id"))
#     date = Column(Date, nullable=False)
#     status = Column(String, nullable=False)

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(50), ForeignKey("employees.employee_id"))
    date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)
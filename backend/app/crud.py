from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.models import Employee, Attendance
from datetime import date

# ---------- EMPLOYEE ----------

def employee_exists(db: Session, employee_id: str, email: str):
    return (
        db.query(Employee)
        .filter(
            (Employee.employee_id == employee_id) |
            (Employee.email == email)
        )
        .first()
    )


def get_all_employees(db: Session):
    return db.query(Employee).order_by(Employee.full_name).all()


def create_employee(db: Session, employee):
    try:
        db_emp = Employee(
            employee_id=employee.employee_id,
            full_name=employee.full_name,
            email=employee.email,
            department=employee.department,
        )
        db.add(db_emp)
        db.commit()
        db.refresh(db_emp)
        return db_emp

    except IntegrityError:
        db.rollback()
        raise ValueError("Employee ID or Email already exists")

    except Exception as e:
        db.rollback()
        raise e

def delete_employee(db: Session, employee_id: str):
    emp = (
        db.query(Employee)
        .filter(Employee.employee_id == employee_id)
        .first()
    )

    if not emp:
        return None

    # ✅ delete dependent attendance first
    db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).delete()

    db.delete(emp)
    db.commit()

    return emp



# ---------- ATTENDANCE ----------

def mark_attendance(db: Session, attendance):
    # 🔍 Validate employee exists
    employee = (
        db.query(Employee)
        .filter(Employee.employee_id == attendance.employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    record = Attendance(
        employee_id=attendance.employee_id,
        date=attendance.date,
        status=attendance.status
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_attendance_by_employee(db: Session, employee_code: str):
    rows = (
        db.query(
            Attendance.id,
            Attendance.date,
            Attendance.status,
            Employee.employee_id.label("employee_code"),
            Employee.full_name.label("employee_name"),
        )
        .join(Employee, Attendance.employee_id == Employee.employee_id)
        .filter(Employee.employee_id == employee_code)
        .order_by(Attendance.date.desc())
        .all()
    )

    return [
        {
            "id": r.id,
            "employee_code": r.employee_code,
            "employee_name": r.employee_name,
            "date": r.date,
            "status": r.status,
        }
        for r in rows
    ]


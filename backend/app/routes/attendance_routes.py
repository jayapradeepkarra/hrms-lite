from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import AttendanceCreate
from app import crud

router = APIRouter()


@router.post("/")
def mark_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):
    return crud.mark_attendance(db, attendance)


@router.get("/{employee_id}")
def get_attendance(
    employee_id: str,
    db: Session = Depends(get_db)
):
    records = crud.get_attendance_by_employee(db, employee_id)

    if not records:
        raise HTTPException(
            status_code=404,
            detail="No attendance records found"
        )

    return records

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import EmployeeCreate
from app.database import get_db
from app import crud

router = APIRouter()

@router.get("")
def list_employees(db: Session = Depends(get_db)):
    return crud.get_all_employees(db)

@router.post("")
@router.post("/")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    try:
        return crud.create_employee(db, employee)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{employee_id}")
def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    emp = crud.delete_employee(db, employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted"}


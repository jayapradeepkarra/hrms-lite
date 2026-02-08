from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.employee_routes import router as employee_router
from app.routes.attendance_routes import router as attendance_router

app = FastAPI(
    title="HRMS Lite API",
    redirect_slashes=False   # ⭐ VERY IMPORTANT
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",
#         "http://127.0.0.1:5173",
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.add_middleware(
    CORSMiddleware," "
    allow_origins=["*"],   # allow all for demo
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_router, prefix="/employees", tags=["Employees"])
app.include_router(attendance_router, prefix="/attendance", tags=["Attendance"])

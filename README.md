# HRMS Lite 🧑‍💼

A lightweight **HR Management System (HRMS Lite)** built using **FastAPI** and **React (Vite)**.  
This application allows an admin to manage employees and track daily attendance.

---

## 🚀 Features

### 👤 Employee Management
- Add new employees
- View all employees
- Delete employees
- Prevent duplicate employee IDs and emails

### 🕒 Attendance Management
- Mark daily attendance (Present / Absent)
- View attendance by employee
- Display employee name along with attendance

---

## 🧰 Tech Stack

### Frontend
- React (Vite)
- Axios
- React Router
- CSS (Custom styling)

### Backend
- FastAPI
- SQLAlchemy
- MS SQL Server
- PyODBC

### Deployment
- Frontend: **Vercel**
- Backend: **Render**

---

## 📂 Project Structure

```text
hrms-lite/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── routes/
│   │       ├── employee_routes.py
│   │       └── attendance_routes.py
│   ├── requirements.txt
│   └── Procfile
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.jsx
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md

cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
python -m uvicorn app.main:app --reload



cd frontend

# Install dependencies
npm install

# Start development server
npm run dev


##Frontend (Vercel)
npm run build

##Backend (Render)
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port $PORT

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# import urllib

# connection_string = urllib.parse.quote_plus(
#     "DRIVER=ODBC Driver 18 for SQL Server;"
#     "SERVER=127.0.0.1,51476;"
#     "DATABASE=HRMS_Lite;"
#     "Trusted_Connection=yes;"
#     "TrustServerCertificate=yes;"
# )

# DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={connection_string}"

# engine = create_engine(
#     DATABASE_URL,
#     echo=True,
#     pool_pre_ping=True
# )

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://hrms_ghnf_user:BLe6y4qaFYhnsb16wy2L75TfockfrKf4@dpg-d646ve6r433s73e52jlg-a/hrms_ghnf"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


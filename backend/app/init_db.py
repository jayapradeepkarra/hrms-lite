from app.database import engine
from app.models import Base
from sqlalchemy.exc import SQLAlchemyError

print("🔄 Starting DB initialization...")

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully")
    except SQLAlchemyError as e:
        print("❌ Database initialization failed")
        raise e

if __name__ == "__main__":
    init_db()

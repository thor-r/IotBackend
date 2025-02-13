from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.base import Base 

# database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# session maker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


from app.models import AudioMetadata  # Importing model here, after Base is defined

# Create the tables in the database
def create_tables():
    """Create database tables based on models."""
    print(f"Using database at: {SQLALCHEMY_DATABASE_URL}")
    try:
        print("Models imported successfully.")
        print(f"Tables in metadata before create_all: {Base.metadata.tables.keys()}")  # Debug: Checking recognized tables
        Base.metadata.create_all(bind=engine)  # Create all tables defined by models
        print("Database tables created successfully.")
        print(f"Tables in metadata after create_all: {Base.metadata.tables.keys()}")  # Confirm table creation
    except Exception as e:
        print(f"Error creating tables: {e}")

if __name__ == "__main__":
    create_tables()
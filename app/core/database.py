from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./task.db"

engine = create_engine(
    DATABASE_URL,
    # shows SQL logs in terminal
    echo=True
)

# Creates a database file tasks.db
# Creates tables automatically based on models
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

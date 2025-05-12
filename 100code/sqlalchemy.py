from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection string
DB_URL = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# SQLAlchemy setup
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()

@as_declarative(metadata=metadata)
class Base:
    id = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()  # Use class name as table name

# Dynamic class to represent objects
class DynamicRecord(Base):
    __abstract__ = True  # Base class for dynamic models

    @classmethod
    def create_table(cls):
        Base.metadata.create_all(bind=engine)

    @classmethod
    def insert_record(cls, **fields):
        """Insert a record into the table."""
        with SessionLocal() as session:
            obj = cls(**fields)
            session.add(obj)
            session.commit()
            return obj

# Example child classes
class Product(DynamicRecord):
    name = Column(String(255))
    price = Column(String(255))

class Customer(DynamicRecord):
    name = Column(String(255))
    email = Column(String(255))

# Initialize tables
Base.metadata.create_all(bind=engine)
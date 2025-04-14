
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from datetime import datetime
import os
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://runner@localhost:5432/mydb")
database = Database(DATABASE_URL)
metadata = MetaData()

# SQLAlchemy engine for migrations
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Goal(Base):
    __tablename__ = "goals"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    category = Column(String(50))  # daily/weekly/monthly
    created_at = Column(DateTime, default=datetime.utcnow)

class Reflection(Base):
    __tablename__ = "reflections"
    
    id = Column(Integer, primary_key=True, index=True)
    goal_id = Column(Integer, ForeignKey("goals.id"), nullable=False)
    rating = Column(Integer)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
def init_db():
    Base.metadata.create_all(bind=engine)

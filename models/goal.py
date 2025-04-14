from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)  # daily/weekly/monthly
    created_at = Column(DateTime, default=func.now(), onupdate=func.now())

    __table_args__ = {'extend_existing': True}  # Add this line
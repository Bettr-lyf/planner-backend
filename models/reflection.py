
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from database import Base

class Reflection(Base):
    __tablename__ = "reflections"
    
    id = Column(Integer, primary_key=True, index=True)
    goal_id = Column(Integer, ForeignKey("goals.id"), nullable=False)
    rating = Column(Integer)
    comment = Column(String)
    created_at = Column(DateTime, default=func.now())

    __table_args__ = {'extend_existing': True}

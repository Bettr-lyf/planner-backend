from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from datetime import datetime
import os
from config import settings

DATABASE_URL = settings.DATABASE_URL.replace('postgresql://', 'postgresql+asyncpg://')

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

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

#  init_db function removed as it's not directly compatible with the async engine.
# Database creation should be handled separately, potentially during application startup.
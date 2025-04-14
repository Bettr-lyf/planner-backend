
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GoalBase(BaseModel):
    title: str
    description: str
    category: str

class GoalCreate(GoalBase):
    pass

class Goal(GoalBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ReflectionBase(BaseModel):
    goal_id: int
    rating: int
    comment: str

class ReflectionCreate(ReflectionBase):
    pass

class Reflection(ReflectionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


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

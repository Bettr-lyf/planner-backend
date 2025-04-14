
from pydantic import BaseModel
from datetime import datetime

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

from pydantic import BaseModel, Field
from datetime import datetime
from models.user import GenderEnum

class UserResponse(BaseModel):
    id: str = Field(..., alias="ulid")
    name: str
    email: str
    gender: GenderEnum
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        validate_by_name = True

class AuthResponse(BaseModel):
    user: UserResponse
    token: str
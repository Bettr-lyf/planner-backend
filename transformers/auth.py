from pydantic import BaseModel, Field
from datetime import datetime
from models.user import GenderEnum

class RegisterResponse(BaseModel):
    id: str = Field(..., alias="ulid")
    name: str
    email: str
    gender: GenderEnum
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
from pydantic import BaseModel, constr, EmailStr
from models.user import GenderEnum

class RegisterRequest(BaseModel):
    name: str = constr(min_length=2, max_length=50)
    email: EmailStr
    password:str = constr(max_length=16, min_length=8)
    gender: GenderEnum
    confirmPassword: str
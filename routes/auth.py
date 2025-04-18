from fastapi import APIRouter
from validators.auth import RegisterRequest
from services.auth import register_user
from transformers.auth import RegisterResponse

router = APIRouter()

@router.post('/register', response_model=RegisterResponse, response_model_by_alias=True)
async def register(payload: RegisterRequest):
	user = await register_user(payload)
	return user

@router.post('/login')
def login():
	return {'message': 'Register user'}

from fastapi import APIRouter
from validators.auth import RegisterRequest, LoginRequest
from services.auth import register_user, login_user
from transformers.auth import AuthResponse

router = APIRouter()

@router.post('/register', response_model=AuthResponse, response_model_by_alias=True)
async def register(payload: RegisterRequest):
	user, token = await register_user(payload)
	return { 'user': user, 'token': token }

@router.post('/login', response_model=AuthResponse)
async def login(payload: LoginRequest):
	user, token = await login_user(payload)
	return { 'user': user, 'token': token }

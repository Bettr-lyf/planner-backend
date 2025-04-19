from fastapi import HTTPException, status
import ulid
from validators.auth import RegisterRequest, LoginRequest
from models.user import User
from utils.security import hash_password, verify_password, generate_token

async def register_user(payload: RegisterRequest):
    """
    Register a new user.
    
    Args:
        payload (RegisterRequest): The user registration data.
        
    Returns:
        UserModel: The created user object.
    """
    hashed_password = hash_password(payload.password)
    payload = payload.model_dump(exclude={'confirmPassword', 'password'})
    user = User(**payload, password=hashed_password, ulid=ulid.new())
    await user.save()
    token = generate_token(user.to_dict(exclude={'password', 'created_at', 'updated_at'}))
    
    return user, token

async def login_user(payload: LoginRequest):
    """
    Authenticate a user.
    
    Args:
        payload (LoginRequest): The user login data.
        
    Returns:
        UserModel: The authenticated user object.
        token: The authentication token.
    """
    user = await User.get_or_none(email=payload.email)
    
    if not user or not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    token = generate_token(user.to_dict(exclude={'password', 'created_at', 'updated_at'}))
    return user, token
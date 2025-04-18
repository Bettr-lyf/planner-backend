import ulid
from validators.auth import RegisterRequest
from models.user import User

async def register_user(payload: RegisterRequest):
    """
    Register a new user.
    
    Args:
        payload (dict): The user registration data.
        
    Returns:
        dict: A message indicating the result of the registration.
    """
    user = User(**payload.model_dump(exclude={'confirmPassword'}), ulid=ulid.new())
    await user.save()
    return user
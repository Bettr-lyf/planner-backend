
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://runner@localhost:5432/mydb"
    
settings = Settings()


import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

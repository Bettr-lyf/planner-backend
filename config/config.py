from pydantic_settings import BaseSettings, SettingsConfigDict
from .classes import JWTConfig, DatabaseConfig

class AppConfig(BaseSettings):
    db: DatabaseConfig = DatabaseConfig()
    jwt: JWTConfig = JWTConfig()

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='DB_',
        extra='allow'
    )
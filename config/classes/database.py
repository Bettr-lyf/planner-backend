from pydantic_settings import BaseSettings, SettingsConfigDict
from . import PostgresConfig

class DatabaseConfig(BaseSettings):
    pg: PostgresConfig = PostgresConfig()

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='DB_',
        extra='allow'
    )
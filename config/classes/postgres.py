from pydantic_settings import BaseSettings, SettingsConfigDict

class PostgresConfig(BaseSettings):
    user: str
    password: str
    host: str
    port: int
    name: str
    client: str

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='DB_',
        extra='allow'
    )
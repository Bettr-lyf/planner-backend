from pydantic_settings import BaseSettings, SettingsConfigDict

class JWTConfig(BaseSettings):
    secret: str
    expiration: int
    algorithm: str = 'HS256'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='JWT_',
        extra='allow'
    )
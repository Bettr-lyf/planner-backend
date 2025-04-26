from tortoise import Tortoise
from . import app_config

TORTOISE_ORM = {
    "connections": {"default": f'{app_config.db.pg.client}://{app_config.db.pg.user}:{app_config.db.pg.password}@{app_config.db.pg.host}:{app_config.db.pg.port}/{app_config.db.pg.name}'},
    "apps": {
        "models": {
            "models": ["models.user", "models.task", "aerich.models"],
            "default_connection": "default",
        },
    },
}

async def init_db():
  await Tortoise.init(config=TORTOISE_ORM)
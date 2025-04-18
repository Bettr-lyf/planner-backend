from tortoise import Tortoise

TORTOISE_ORM = {
    "connections": {"default": 'postgres://postgres:1234567890@localhost:5432/bettr_lyf'},
    "apps": {
        "models": {
            "models": ["models.user", "models.task", "aerich.models"],
            "default_connection": "default",
        },
    },
}

async def init_db():
  await Tortoise.init(config=TORTOISE_ORM)
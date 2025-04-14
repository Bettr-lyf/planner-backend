TORTOISE_ORM = {
    "connections": {"default": 'postgres://postgres:1234567890@localhost:5432/bettr_lyf'},
    "apps": {
        "models": {
            "models": ["models.task", "aerich.models"],
            "default_connection": "default",
        },
    },
}
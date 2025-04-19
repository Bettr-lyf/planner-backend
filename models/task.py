from packages.base_model import BaseModel
from tortoise import fields

class Task(BaseModel):
    id = fields.IntField(pk=True)
    ulid = fields.UUIDField(unique=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    due_date = fields.DatetimeField(null=True)
    priority = fields.IntField(default=1)
    status = fields.IntField(default=1)
    completed = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "tasks"
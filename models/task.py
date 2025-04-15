from tortoise.models import Model
from tortoise import fields

class Task(Model):
    id = fields.IntField(pk=True)
    ulid = fields.UUIDField(default=uuid.uuid4, unique=True)

    title = fields.CharField(max_length=255)
    priority = fields.CharEnumField(enum_type=str, enum_values=["low", "medium", "high"], default="medium")
    category = fields.CharEnumField(enum_type=str, enum_values=["daily", "weekly", "monthly"], default="daily")
    status = fields.CharEnumField(enum_type=str, enum_values=["pending", "completed"], default="pending")

    time_estimate_minutes = fields.IntField(default=0)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    user = fields.ForeignKeyField("models.User", related_name="tasks", on_delete=fields.CASCADE)
    
    class Meta:
        table = "tasks"
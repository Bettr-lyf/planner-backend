from enum import IntEnum
from tortoise import fields

from packages.base_model import BaseModel

class GenderEnum(IntEnum):
    MALE = 0
    FEMALE = 1

class User(BaseModel):
    id = fields.IntField(pk=True)
    ulid = fields.CharField(max_length=26, unique=True)
    name = fields.CharField(max_length=255)
    gender = fields.IntEnumField(GenderEnum, null=False)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"
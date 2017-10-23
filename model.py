# -*- coding:utf-8 -*-

from schematics.models import Model
from schematics.types import StringType, EmailType, BooleanType, IntType, ListType, ModelType

class UserModel(Model):
    users_id = IntType()
    first_name = StringType(required=True)
    last_name = StringType(required=True)
    email = EmailType(required=True)
    nickname = StringType(required=True)
    password = StringType(required=True)

class UserAddModel(Model):
    age = IntType()
    phone = StringType()
    address = StringType()
    photo = StringType()
    ava = StringType()
    sex = IntType()
    user_id = ModelType(UserModel)


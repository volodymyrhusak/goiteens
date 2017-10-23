# -*- coding:utf-8 -*-

from schematics.models import Model
from schematics.types import StringType, EmailType, BooleanType, IntType, ListType, ModelType, DateTimeType
from datetime import datetime


class UserType(Model):
    id = IntType(required=True)
    name = StringType(required=True)
    create_time = DateTimeType(required=True, default=datetime.now())


class UserModel(Model):
    id = IntType(required=True)
    first_name = StringType(required=True)
    last_name = StringType(required=True)
    type = ModelType(UserType, required=True)
    descr = StringType(required=False, default='')
    user_photo = StringType(required=False, default='')
    user_photos = ListType(StringType, required=False, default=[])
    email = EmailType(required=True)
    nickname = StringType(required=True)
    password = StringType(required=True)
    create_time = DateTimeType(required=True, default=datetime.now())


class UserAddModel(Model):
    id = IntType()
    age = IntType(default=None)
    create_time = DateTimeType(required=True, default=datetime.now())
    phone = StringType(default=None)
    address = StringType(default=None)
    photo = StringType(default=None)
    ava = StringType(default=None)
    sex = IntType(default=None)
    user = ModelType(UserModel)


class GroupUserModel(Model):
    id = IntType()
    group = ModelType(UserModel)
    user = ModelType(UserModel)
    create_time = DateTimeType(required=True, default=datetime.now())


class PostModel(Model):
    id = IntType()
    title = StringType(required=True)
    photos = ListType(StringType, required=False, default=[])
    text = StringType(required=False, default=None)
    likes = IntType(required=True, default=0)
    user = ModelType(UserModel)
    create_time = DateTimeType(required=True, default=datetime.now())


class CommentsModel(Model):
    id = IntType()
    text = StringType(required=False, default=None)
    likes = IntType(required=True, default=0)
    user = ModelType(UserModel)
    create_time = DateTimeType(required=True, default=datetime.now())


class PostCommentModel(Model):
    id = IntType()
    post = ModelType(PostModel)
    comment = ModelType(CommentsModel)
    create_time = DateTimeType(required=True, default=datetime.now())


class MessegeModel(Model):
    id = IntType()
    user_from = ModelType(UserModel)
    user_to = ModelType(UserModel)
    is_read = BooleanType(required=True, default=False)
    create_time = DateTimeType(required=True, default=datetime.now())


if __name__ == '__main__':
    type = UserType()
    type.id = 1
    type.name = 'test'

    user = UserModel()
    user.id = 1
    user.first_name = 'test'
    user.last_name = 'test'
    user.type = type
    user.descr = 'test'
    user.user_photo = 'test'
    user.user_photos = ['test']
    user.email = 'test@test.test'
    user.nickname = 'test'
    user.password = 'test'

    print(user.values())
    print(user.validate())

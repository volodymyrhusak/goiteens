# -*- coding:utf-8 -*-
from models.models import UserModel, UserAddModel, UserType
from models.executeSqlite3 import executeSelectOne, executeSelectAll, executeSQL


class UserManager():
    user_type = UserType()
    user_type.id = 1
    user_type.id = 'user'

    def __init__(self):
        self.user = UserModel()

    def getModelFromForm(self,form):
        self.user.first_name = form.get('first_name', '')
        self.user.last_name = form.get('last_name', '')
        self.user.type = self.user_type
        self.user.email = form.get('email', '')
        self.user.nickname = form.get('name', '')
        if form.get('passw1', '') == form.get('passw2', ''):
            self.user.password = form.get('passw1', '')
        return self

    def check_user(self):
        sql = 'SELECT * FROM users WHERE nickname = "{}" or email = "{}"'.format(self.user.nickname, self.user.email)
        check_user = executeSelectOne(sql)
        if check_user:
            return True
        return False


    def addNewUser(self):
        sql = 'INSERT INTO users (first_name, last_name, type, email, nickname, password, create_time) VALUES ("{}","{}","{}","{}","{}","{}","{}")' \
            .format(self.user.first_name, self.user.last_name, self.user_type,
                    self.user.email, self.user.nickname, self.user.password, self.user.create_time)
        return executeSQL(sql)

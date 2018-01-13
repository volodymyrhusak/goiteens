# -*- coding:utf-8 -*-
class BoolWhere():

    def __init__(self, manager):
        self.manager = manager
        self.sql = ''

    def And(self, args):
        result = ' AND {}' * len(args)
        result = result.format(*self.parse_args(args))
        self.sql += result
        return self

    def Or(self, args):
        result = ' OR {}' * len(args)
        result = result.format(*self.parse_args(args))
        self.sql += result
        return self

    def Not(self, args):
        result = ' NOT {}' * len(args)
        result = result.format(*self.parse_args(args))
        self.sql += result
        return self

    def Limit(self, args1, args2):
        result = ' LIMIT {}, {}'.format(args1,args2)
        self.sql += result
        return self

    def parse_args(self, args):
        return [self.template.format(arg[0], arg[1], repr(arg[2])) for arg in args]

class BoolWhereSelect(BoolWhere):
    select_sql_from = 'SELECT * FROM {} '
    select_sql_where = 'WHERE {} '
    template = '{0} {1} {2} '

    def __init__(self, manager, sql):
        super(BoolWhereSelect, self).__init__(manager)
        self.select_sql_where = self.select_sql_where.format(sql)
        self.sql = self.select_sql_from.format(self.manager.object._name) + self.select_sql_where

    def run(self):
        print(self.sql)
        return self.manager.fillModel(self.sql)


class BoolWhereDelete(BoolWhere):
    select_sql_from = 'DELETE FROM {} '
    select_sql_where = 'WHERE {} '
    template = '{0} {1} {2} '

    def __init__(self, manager, sql):
        super(BoolWhereDelete, self).__init__(manager)
        self.select_sql_where = self.select_sql_where.format(sql)
        self.sql = self.select_sql_from.format(self.manager.object._name) + self.select_sql_where

    def run(self):
        print(self.sql)
        return self.manager._delete(self.sql)
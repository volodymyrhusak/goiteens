# -*- coding:utf-8 -*-

import sqlite3


def executeSelectOne(sql):
    conn = sqlite3.connect('my_db.sqlite3')
    curs = conn.cursor()
    curs.execute(sql)
    data = curs.fetchone()
    conn.close()
    return data

def executeSelectAll(sql):
    conn = sqlite3.connect('my_db.sqlite3')
    curs = conn.cursor()
    curs.execute(sql)
    data = curs.fetchall()
    conn.close()
    return data

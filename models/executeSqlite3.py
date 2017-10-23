# -*- coding:utf-8 -*-


from models import conn

def executeSelectOne(sql):

    curs = conn.cursor()
    curs.execute(sql)
    data = curs.fetchone()

    return data

def executeSelectAll(sql):

    curs = conn.cursor()
    curs.execute(sql)
    data = curs.fetchall()

    return data

def executeSQL(sql):
    try:
        curs = conn.cursor()
        curs.execute(sql)
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


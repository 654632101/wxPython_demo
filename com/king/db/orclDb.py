# -*- encoding:utf-8 -*-
import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
class orclDb():
   def __init__(self, name='scott', password='king', serverName='ORCL'):
       self.name = name
       self.password = password
       self.serverName = serverName
    # 创建连接
   def conDb(self):
       print '连接数据库'
       db = cx_Oracle.connect(self.name, self.password, self.serverName)
       return db
   # 获取带条件的查询语句
   def queryDatas(self, db, sql, parms):
       cur = db.cursor()
       rs = cur.execute(sql, parms)
       cur.close()
       return rs
   # 执行无条件的查询语句
   def queryData(self, db, sql):
       cur = db.cursor()
       rs = cur.execute(sql).fetchall() 
       cur.close()
       return rs
   # 插入数据
   def insertData(self, db, sql, parms):
       cur = db.cursor()
       try:
           cur.execute(sql, parms)
           db.commit()
           cur.close()
       except:
           return -1
       return 1
   # 关闭数据库连接
   def closeDb(self, db):
       db.close()
#        
# dataStore = orclDb()
# orcl_db = dataStore.conDb()
# print orcl_db
# reslos = dataStore.queryData(orcl_db, 'select * from emp')
# print "print all:(%s)" % reslos

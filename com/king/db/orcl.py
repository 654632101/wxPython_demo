# -*- encoding:utf-8 -*-
import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
db = cx_Oracle.connect('scott', 'king', 'ORCL')
print db
dsn_tns = cx_Oracle.makedsn('127.0.0.1', '1521', 'ORCL')
print dsn_tns
print db.version
cur = db.cursor()
sql = 'select * from emp'
print cur.execute(sql)
rs = cur.fetchall() 
print "print all:(%s)" % rs
insert_sql = "INSERT INTO Tb_BUG_INFO (RID,Bug_Type,Query_Info,bug_data) VALUES(TB_BUG_SEQ.NEXTVAL,:type,:query,sysdate)"
print "\n print by row:"
pram =['莹','软件']
cur.execute(insert_sql,pram)
db.commit()
for x in rs:
    print x
    print x[2]
    print x[4]

db.close()
str = '你好:不好'
strs = str.split(':')
print strs
print strs[0]
print strs[1]

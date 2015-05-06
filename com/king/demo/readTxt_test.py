# coding=gbk
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

pattern = re.compile(r'udolink note+')
w = open("over.txt", 'w+')
w.truncate()
f = open("log.txt", 'r')
w.truncate()
line = f.readline().decode("gbk")
while line:
    que = re.match(r' http', line,)
    select = re.match(r' UDOLink StoreManager Note+', line,)
    if que:
        print "http:", que.string,
        w.write(que.string,)
    if select:
        saixun = re.match(r'.*Ljava.', select.string,)
        role = re.match(r'.*org_roles_inf.', select.string)
        
        if saixun:
#             print "delete", saixun.string,
           print '.....'
        else:
            if role:
                print '========'
            else:
                print   "sql:", select.string,
                w.write(select.string,)
    match = pattern.match(line,)
    line = f.readline().decode("gbk")
    
w.close()
f.close()


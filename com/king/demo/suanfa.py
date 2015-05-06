def pri(qq):  
    print qq
    
q = [0, 6, 3, 1, 7, 5, 8, 9, 2, 4]
head = 1
tail = 10
over = []
try:
    while(head < tail):
        print "num:" , len(q) , "tail:" , tail , "head:" , head
        print q[head]
        over.append(q[head])
        pri(q)
        head += 1
        print "insert :" , head , "long : " , len(q)
        q.append(q[head])
        tail += 1
        head += 1
except Exception, ex: 
     print "======================================================="      
     print Exception, ":", ex   
     print "======================================================="       
    
print "over : " , over
